import matplotlib.pyplot as plt
import math
import copy
import sys
inf_d = 20
win_size = 20
N = 14 #number of points
text_x=4
text_y=10
text = "This Polygon needs at least two gaurds."
font_size=12

#TODO: A function is_circular
#TODO: If the number of vertices is less than or equal to 3, 
#TODO: Remove all straight edges
#TODO: Constant size window.

class Node(object):
    def __init__(self, num, x, y):
        self.v_num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def print(self):
        print(self.x,self.y)

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def append_head(self,node):
        if(self.head is None):
            self.head = node
            self.tail= node
        else:
            node.left = self.head.left
            node.right = self.head
            self.head.left = node
            self.head = node

    def append_k(self,node):
        if(self.head is None):
            self.tail = self.head = node
        else:
            node.right = self.tail
            self.tail.left = node
            self.tail = node

    def append_tail(self,node,make_circular=False):
        if(self.head is None):
            self.head = node
            return
        is_circular = self.head.left is not None

        if(is_circular):
            node.right=self.head
            node.left = self.head.left
            self.head.left.right = node
            self.head.left = node
        else:
            temp = self.head
            while(temp.right is not None):
                temp = temp.right
            node.left = temp
            temp.right=node
        if(make_circular):
            node.right=self.head
            self.head.left = node

    def delete_node(self,node):
        if(self.head is None):
            print("empty list")
            return

        is_circular = self.head.left is not None

        if(is_circular):
            temp = self.head.right
            while(temp!=self.head and temp!=node):
                temp = temp.right
        else:
            temp = self.head
            while(temp is not None and temp != node):
                temp=temp.right

        if(temp==node):
            if self.head==node:
                self.head = self.head.right
            if temp.left is not None:
                temp.left.right = node.right
            if temp.right is not None:
                temp.right.left = node.left
        else:
            print("Unable to delete node")
    def plot(self):
        circular = self.head.left is not None
        x = []
        y = []
        if(circular):
            temp = self.head.right
            x.append(self.head.x)
            y.append(self.head.y)
            while temp != self.head:
                x.append(temp.x)
                y.append(temp.y)
                temp=temp.right
            x.append(x[0])
            y.append(y[0])
        else:
            temp=self.head
            while temp is not None:
                x.append(temp.x)
                y.append(temp.y)
                temp=temp.right
        plt_polygon(x,y)
    
    def kplot(self):
        x = []
        y = []
        if(self.head == self.tail and self.head.right is not None and self.tail.left is not None):
            temp = self.head.left
            x.append(self.head.x)
            y.append(self.head.y)
            while temp != self.head:
                x.append(temp.x)
                y.append(temp.y)
                temp=temp.left
            x.append(x[0])
            y.append(y[0])
        else:
            temp=self.head
            while temp is not None:
                x.append(temp.x)
                y.append(temp.y)
                temp=temp.left
        plt_polygon(x,y)
    def first_reflex_node(self):
        temp = self.head.right
        node = None
        while(temp!= self.head): #reflex test is always for a circular list
            if(ccw(temp.left,temp,temp.right) <0 ):# we will remove all straight edges. degenerate, ignore for now
                node = temp
                break
            temp = temp.right
        return node

    def reset_v_num(self,node):
        temp = self.head.right
        while(temp!=self.head):
            if temp == node:
                break
            temp = temp.right

        if(temp == node):
            i = 0
            node.v_num = i
            self.head = node
            temp = temp.right
            while(temp!=node):
                i+=1
                temp.v_num = i
                temp = temp.right
        else:
            print("the reflex edge vertex doesn't exist.")
"""
    def print(self):
        temp = self.head

        #print("v_num:%d\t(x,y):(%d,%d)\n"%(temp.v_num,temp.x,temp.y))
        print("printing datastructure")
        temp = temp.right
        temp.print()

        while(temp!=self.head and temp.right is not None):
            #print("v_num:%d\t(x,y):(%d,%d)\n"%(temp.v_num,temp.x,temp.y))
            temp.print()
            temp = temp.right
"""

def is_reflex(node):
    return ccw(node.left,node,node.right) <0 


#division by zero error, robust
def intersection(a,b,c,d):
    dtr = ((b.x-a.x)*(d.y-c.y)-(b.y-a.y)*(d.x-c.x))
    if(math.isclose(dtr,0)):
        print("lines are parallel.degenerate case")
        return None
    r = ((a.y-c.y)*(d.x-c.x)-(a.x-c.x)*(d.y-c.y))/dtr
    s = ((a.y-c.y)*(b.x-a.x)-(a.x-c.x)*(b.y-a.y))/dtr
#    if((r >0 or math.isclose(r,0)) and (r<1 or math.isclose(r,1)) and (s>0 or math.isclose(s,0)) and (s<1 or math.isclose(s,1))):
    if(r >=0 and r<=1  and s>=0 and s<=1 ):
        return (a.x+r*(b.x-a.x),a.y+r*(b.y-a.y))
    elif(is_between(a,c,b)):
        return (c.x,c.y)
    elif(is_between(a,d,b)):
        return (d.x,d.y)
    else:
        return None

def ccw(a,b,c):
	return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)


def plt_polygon(x,y):
    plt.plot(x,y)
    #plt.show()

def inf_coord(a,b, along_b = False):
    v = (b.x - a.x, b.y - a.y)
    v_mod = math.sqrt(v[0]**2+v[1]**2)
    u = (v[0]/v_mod,v[1]/v_mod)
    if(along_b):
        p = (a.x + inf_d*u[0],a.y + inf_d*u[1])
    else:
        p = (a.x - inf_d*u[0],a.y - inf_d*u[1])
    return p

def distance(a,b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_between(a,c,b):
    return math.isclose(distance(a,c) + distance(c,b), distance(a,b))

def display():
    plt.axis([0,win_size,0,win_size])
    plt.plot(F1.x,F1.y,marker='o', c='k')
    plt.plot(L1.x,L1.y,marker='o', c='b')
    plt.plot(vi.x,vi.y,marker='x',c='r')
    P.plot()
    K.kplot()
    plt.show()

"""
a = Node(0,15.866935483870968,5.232683982683984)
b = Node(0,-6.321148797313381,7.093697545229208)
c = Node(0,22.24035695862105,18.020950432975354)

print(ccw(a,b,c))
"""

print("Please click")
plt.axis([0,win_size,0,win_size])
plt.plot()
inpt = plt.ginput(N,show_clicks=True)
print("clicked", inpt)
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]


#inpt = [(2,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(4,11),(2,11.5),(3,8.5),(3,6),(0,4)]
"""
#inpt = [(3,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(2,11.5),(3,8.5),(3,6),(4,4)]
inpt = [(1,1),(2,2),(1,3),(0,2)] #convex 
#inpt = [(2,2),(4,6),(2,3),(1,4)]
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]
#plt_polygon(x,y) 
"""
#inpt = [(1.723790322580645, 2.8192640692640696), (4.737903225806452, 4.0909090909090917), (8.4778225806451601, 1.5476190476190479), (8.5181451612903221, 6.8641774891774894), (2.0766129032258065, 9.7997835497835517), (0.42338709677419351, 3.9826839826839828)]
#inpt = [(3.588709677419355, 3.4199134199134198), (6.4919354838709671, 5.6926406926406923), (13.608870967741936, 5.4220779220779232), (15.866935483870968, 5.2326839826839837), (16.693548387096772, 10.50865800865801), (11.068548387096772, 11.212121212121213), (9.3951612903225801, 17.353896103896105), (3.9516129032258061, 18.354978354978357), (8.125, 13.511904761904763), (2.520161290322581, 10.535714285714286), (1.55241935483871, 7.1807359307359313), (1.028225806451613, 1.3365800865800868)]
inpt = [(3.245967741935484, 3.5010822510822512), (8.3266129032258078, 2.337662337662338), (8.3266129032258078, 5.6114718614718626), (11.471774193548388, 5.3138528138528152), (15.544354838709676, 2.283549783549784), (19.254032258064516, 4.258658008658009), (19.052419354838708, 8.0735930735930737), (18.608870967741936, 11.780303030303031), (10.362903225806452, 12.754329004329005), (5.1814516129032251, 13.701298701298704), (4.05241935483871, 18.030303030303031), (0.94758064516129004, 17.813852813852815), (3.125, 13.863636363636367), (2.0161290322580649, 9.9404761904761916)]
#inpt = [(3.286290322580645, 4.3939393939393945), (3.3266129032258061, 8.0465367965367971), (4.9395161290322589, 8.317099567099568), (7.338709677419355, 6.9372294372294387), (10.58467741935484, 2.7164502164502169), (9.7983870967741922, 10.806277056277057), (15.06048387096774, 8.9123376623376629), (16.3508064516129, 4.2857142857142865), (16.794354838709676, 12.240259740259742), (10.362903225806452, 16.352813852813856), (8.2056451612903238, 14.458874458874462), (3.911290322580645, 15.135281385281388), (3.024193548387097, 18.030303030303031), (1.895161290322581, 14.269480519480521)]
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]

P = DoublyLinkedList()

n = len(inpt)

for i,pt in enumerate(inpt):
    node = Node(i,pt[0],pt[1])
    P.append_tail(node)

#hack to avoid multiple ifs
P.delete_node(node)
P.append_tail(node, make_circular=True)
P.plot()
plt.axis([0,win_size,0,win_size])
plt.show()


r_node = P.first_reflex_node()

if(r_node is None):
    print("This polygon is convex. It can be gaurded by a single gaurd and the kernel of the polygon is itself.")
    plt.axis([0,win_size,0,win_size])
    plt.show()
    sys.exit()

P.reset_v_num(r_node) #r_node is the self.head node


vi = r_node

K = DoublyLinkedList()


F1 = inf_coord(vi,vi.right) #1st edge. infinity-r_node
L1 = inf_coord(vi,vi.left) #2nd edge. r_node-infinity


F1 = Node(0,F1[0],F1[1])
L1 = Node(1,L1[0],L1[1])
K.append_k(F1)
K.append_k(copy.deepcopy(vi))
K.append_k(L1)


vi = vi.right


i = 1
while(i<=n-3):
    display()
    if(is_reflex(vi)): #vertex i is reflex
        vi_next_inf = inf_coord(vi,vi.right)
        vi_next_inf = Node(0,vi_next_inf[0],vi_next_inf[1])
        left_test = ccw(vi_next_inf,vi.right, F1)
        if(left_test<0 or math.isclose(left_test,0)): #F1 lies on or right of the vi+1 to inf line
            p = None
            q = None
            wt1 = F1
            wt2 = F1.left
            while(wt1!=L1):
                p = intersection(wt2,wt1,vi.right,vi_next_inf)
                if(p is not None):
                    w_d = Node(0,p[0],p[1])
                    break
                wt1 = wt2
                wt2 = wt2.left
            if(wt1==L1):
                plt.text(text_x,text_y,text,fontsize=font_size)
                display()
                print("Solution doesn't exist")
                sys.exit(0)
            ws2 = F1
            ws1 = F1.right
            while(ws1 is not None):
                q = intersection(ws2,ws1,vi.right,vi_next_inf)
                if(q is not None):
                    w_dd = Node(0,q[0],q[1])
                    break
                ws2 = ws1
                ws1 = ws1.right
            if(q is None):
                tail_end2 = K.tail
                tail_end1 = tail_end2.right
                head_end = K.head

                #product of two left tests should be the same=> slope within the slopes of end half lines
                if((ccw(tail_end1,tail_end2,vi_next_inf)  * ccw(vi.right,vi_next_inf, head_end)) > 0): #slope is comprised bw the slopes of the two half lines
                    wt2.right = w_d
                    w_d.left = wt2
                    w_d.right = vi_next_inf
                    vi_next_inf.left = w_d
                    #vi_next_inf.right = None
                    K.head = vi_next_inf
                #if slope is not comprised withing the two end half lines, the edge will pierce the current K at two points making it bounded.
                else:
                    wr2 = K.tail
                    wr1 = K.tail.right
                    while(True): #warning
                        q = intersection(wr1,wr2,vi.right,vi_next_inf)
                        if(q is not None):
                            w_dd = Node(0,q[0],q[1])
                            break
                    wt2.right = w_d
                    w_d.left = wt2
                    w_d.right = w_dd
                    w_dd.left = w_d
                    w_dd.right = wr1
                    wr1.left = w_dd
                    K.tail = K.head = wt2 # K is bounded now. should head be wt2?
            else:
                w_d.left = wt2
                wt2.right = w_d
                w_d.right = w_dd
                w_dd.left = w_d
                w_dd.right = ws1
                ws1.left = w_dd
                if(K.head==K.tail):
                    K.head = K.tail = w_d

            if(q is None):
                F1 = vi_next_inf
            else:
                F1 = w_dd
            #case 11
            w1 = L1
            w2 = L1.left
            while(w2 is not None):
                if(ccw(vi.right,w1,w2)>0):
                    L1 = w1
                    break
                w1 = w2
                w2 = w2.left

        #Ki+1 = Ki since the intersection of the new half plane and the current kernel is the current kernel itself
        else:
            #case 12 F1
            w1 = F1
            w2 = F1.left
            while(w2 is not None):
                if(ccw(vi.right,w1,w2)<0):
                    F1 = w1
                    break
                w1 = w2
                w2 = w2.left
            #case 11 L1
            w1 = L1
            w2 = L1.left
            while(w2 is not None):
                if(ccw(vi.right,w1,w2)>0):
                    L1 = w1
                    break
                w1=w2
                w2=w2.left
        
    else:
        vi_next_inf = inf_coord(vi,vi.right,along_b=True)
        vi_next_inf = Node(0,vi_next_inf[0],vi_next_inf[1])
        if(ccw(vi,vi_next_inf,L1)>0): # L1 is to the left. Ki+1 = Ki
            #case 12 F1
            w1 = F1
            w2 = F1.left
            while(w2 is not None):
                if(ccw(vi.right,w1,w2)<0):
                    F1 = w1
                    break
                w1 = w2
                w2 = w2.left
            if(K.head == K.tail and K.head.right is not None and K.tail.left is not None): #bounded
                #case 11 L1
                w1 = L1
                w2 = L1.left
                while(w2 is not None):
                    if(ccw(vi.right,w1,w2)>0):
                        L1 = w1
                        break
                    w1=w2
                    w2=w2.left
        else:
            p = None
            q = None
            wt2 = L1
            wt1 = L1.right
            while(wt2!=F1):
                p = intersection(wt2,wt1,vi,vi_next_inf)
                if(p is not None):
                    w_d = Node(0,p[0],p[1])
                    break
                wt2 = wt1
                wt1 = wt1.right
            if(wt2==F1):
                plt.text(text_x,text_y,text,fontsize=font_size)
                display()
                print("Solution doesn't exist")
                sys.exit(0)
            ws1 = L1
            ws2 = L1.left
            while(ws2 is not None):
                q = intersection(ws1,ws2,vi,vi_next_inf)
                if(q is not None):
                    w_dd = Node(0,q[0],q[1])
                    break
                ws1 = ws2
                ws2 = ws2.left
            if(q is None):
                tail_end2 = K.tail
                tail_end1 = tail_end2.right
                head_end = K.head
                if((ccw(tail_end1,tail_end2,vi_next_inf)  * ccw(vi,vi_next_inf, head_end)) > 0): #slope is comprised bw the slopes of the two half lines
                    wt1.left = w_d
                    w_d.right = wt1
                    w_d.left = vi_next_inf
                    vi_next_inf.right = w_d
                    #vi_next_inf.left = None
                    K.tail = vi_next_inf #vi_next_inf is the head?
                else:
                    wr1 = K.head
                    wr2 = wr1.left
                    while(True):
                        q = intersection(wr1,wr2,vi,vi_next_inf)
                        if(q is not None):
                            w_dd = Node(0,q[0],q[1])
                            break
                        wr1 = wr2
                        wr2 = wr2.left
                    wr2.right = w_dd
                    w_dd.left = wr2
                    w_dd.right = w_d
                    w_d.left = w_dd
                    w_d.right = wt1
                    wt1.left = w_d
                    K.tail = K.head = wr2
            else:
                w_d.left = w_dd
                w_d.right = wt1
                w_dd.right = w_d
                w_dd.left = ws2
                wt1.left = w_d
                ws2.right = w_dd
                if(K.head==K.tail):
                    K.head = K.tail = w_d

            #update F1 and L1
            if(q is None):
                L1 = vi_next_inf
                if(is_between(vi,vi.right,w_d)):
                    #case 12 F1
                    w1 = F1
                    w2 = F1.left
                    while(w2 is not None):
                        if(ccw(vi.right,w1,w2)<0):
                            F1 = w1
                            break
                        w1 = w2
                        w2 = w2.left
                else:
                    F1= w_d
            else:
                if(is_between(vi,vi.right,w_d)):
                    #case 12 F1
                    w1 = F1
                    w2 = F1.left
                    while(w2 is not None):
                        if(ccw(vi.right,w1,w2)<0):
                            F1 = w1
                            break
                        w1 = w2
                        w2 = w2.left
                else:
                        F1 = w_d
                if(is_between(vi,vi.right,w_dd)):
                    L1 = w_dd
                else:
                    #case 11 w_dd
                    w1 = w_dd
                    w2 = w_dd.left
                    while(w2 is not None):
                        if(ccw(vi.right,w1,w2)>0):
                            L1 = w1
                            break
                        w1=w2
                        w2=w2.left

    vi=vi.right
    i+=1

P.plot()
K.kplot()

plt.axis([0,win_size,0,win_size])
plt.show()


"""
use of vector algebra
use of math.isclose to avoid floating point errors.
consistency in variable naming
a single data structure that handles the transformation of a doubly linked list to a circular list.
avoid slope tests, angle tests suggested in the paper with left tests.
"""
