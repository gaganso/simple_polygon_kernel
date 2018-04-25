import matplotlib.pyplot as plt
import math
import copy
import sys
inf_d = 10

#TODO: A function is_circular
#TODO: If the number of vertices is less than or equal to 3, 
#TODO: Remove all straight edges

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
    
    def kplot(self,n):
        circular = self.head.left is not None
        x = []
        y = []

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


def is_reflex(node):
    return ccw(node.left,node,node.right) <0 


#division by zero error, robust
def instersection(a,b,c,d):
    dtr = ((b.x-a.x)*(d.y-c.y)-(b.y-a.y)*(d.x-c.x))
    if(math.isclose(dtr,0)):
        print("lines are parallel.degenerate case")
        return None
    r = ((a.y-c.y)*(d.x-c.x)-(a.x-c.x)*(d.y-c.y))/dtr
    s = ((a.y-c.y)*(b.x-a.x)-(a.x-c.x)*(b.y-a.y))/dtr
    print("r and s")
    print(r,s)
#    if((r >0 or math.isclose(r,0)) and (r<1 or math.isclose(r,1)) and (s>0 or math.isclose(s,0)) and (s<1 or math.isclose(s,1))):
    if(r >=0 and r<=1  and s>=0 and s<=1 ):
        return (a.x+r*(b.x-a.x),a.y+r*(b.y-a.y))
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


print("Please click")
plt.axis([0,10,0,10])
plt.plot()
inpt = plt.ginput(6,show_clicks=True)
print("clicked", inpt)
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]


inpt = [(2,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(4,11),(2,11.5),(3,8.5),(3,6),(0,4)]
"""
#inpt = [(3,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(2,11.5),(3,8.5),(3,6),(4,4)]
inpt = [(1,1),(2,2),(1,3),(0,2)] #convex 
#inpt = [(2,2),(4,6),(2,3),(1,4)]
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]
#plt_polygon(x,y) 
"""
#inpt = [(1.723790322580645, 2.8192640692640696), (4.737903225806452, 4.0909090909090917), (8.4778225806451601, 1.5476190476190479), (8.5181451612903221, 6.8641774891774894), (2.0766129032258065, 9.7997835497835517), (0.42338709677419351, 3.9826839826839828)]
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
plt.show()


r_node = P.first_reflex_node()

if(r_node is None):
    print("the polygon is convex. It can be gaurded by a single gaurd and the whole of the polygon is its kernel.")
    plt.show()
    sys.exit()

P.reset_v_num(r_node) #r_node is the self.head node


vi = r_node

K = DoublyLinkedList()


F1 = inf_coord(vi,vi.right) #1st edge. infinity-r_node
L1 = inf_coord(vi,vi.left) #2nd edge. r_node-infinity

print(F1,L1)
print((F1[1]-vi.y)/(F1[0]-vi.x))
print((vi.right.y-vi.y)/(vi.right.x-vi.x))

print((L1[1]-vi.y)/(L1[0]-vi.x))
print((vi.left.y-vi.y)/(vi.left.x-vi.x))


F1 = Node(0,F1[0],F1[1])
L1 = Node(1,L1[0],L1[1])
K.append_head(F1)
K.append_head(copy.deepcopy(vi))
K.append_head(L1)


vi = vi.right
#K1 is done


#loop through all the vertices now

print(is_reflex(vi))

i = 1


    
plt.plot(F1.x,F1.y,marker='o', c='k')
plt.plot(L1.x,L1.y,marker='o', c='b')
plt.plot(vi.x,vi.y,marker='x',c='r')
P.plot()
K.plot()
plt.show()
while(i<n-1):

    if(is_reflex(vi)): #vertex i is reflex
        vi_next_inf = inf_coord(vi,vi.right)
        vi_next_inf = Node(0,vi_next_inf[0],vi_next_inf[1])

        #F1 lies on or left of the vi+1 to inf line
        left_test = ccw(vi_next_inf,vi.right,F1)
        if(left_test<0 or math.isclose(left_test,0)):
            p = None
            q = None
            wt1 = F1
            wt2 = F1.left
            while(wt1!=L1):
                p = instersection(wt2,wt1,vi.right,vi_next_inf)
                if(p is not None):
                    w_d = Node(0,p[0],p[1])
                    break
                wt1 = wt2
                wt2 = wt2.left
            if(wt1==L1):
                print("Solution doesn't exist")
                sys.exit(0)
            ws2 = F1
            ws1 = F1.right
            while(ws1 is not None and ws1.right is not None):
                q = instersection(ws1,ws2,vi.right,vi_next_inf)
                if(q is not None):
                    w_dd = Node(0,q[0],q[1])
                    break
                ws2 = ws1
                ws1 = ws1.right
            if(q is None):
                #find tail and head end to find if the edge under consideration is comprised withing the slopes of the two infinity lines
                l_end1=L1
                if(L1.left is not None):
                    l_end2 = L1.left
                else:
                    l_end1 = L1.right
                    l_end2 = L1
                while(l_end2.left is not None):
                    l_end1 = l_end2
                    l_end2 = l_end2.left
                r_end = F1
                while(r_end.right is not None):
                    r_end = r_end.right
                #product of two left tests should be the same=> slope within the slopes of end half lines
                if((ccw(l_end1,l_end2,vi_next_inf)  * ccw(vi.right,vi_next_inf, r_end)) > 0): #slope is comprised bw the slopes of the two half lines
                    wt2.right = w_d
                    w_d.left = wt2
                    w_d.right = vi_next_inf
                    vi_next_inf.left = w_d
                #if slope is not comprised withing the two end half lines, the edge will pierce the current K at two points making it bounded.
                else:
                    tail = L1
                    while(tail.left is not None):
                        tail = tail.left
                    wr2 = tail
                    wr1 = tail.right
                    while(wr1.right is not None):
                        q = instersection(wr1,wr2,vi.right,vi_next_inf)
                        if(q is not None):
                            w_dd = Node(0,q[0],q[1])
                            break

                    wt2.right = w_d
                    w_d.left = wt2
                    w_d.right = w_dd
                    w_dd.left = w_d
                    w_dd.right = wr1
                    wr1.left = w_dd
                    K.head = wt2
    
                    #change Ki
                    #list becomes circular. change head to tail when Ki becomes bounded
            else:
                w_d.left = wt2
                w_d.right = w_dd
                w_dd.left = w_d
                w_dd.right = ws1
                wt2.right = w_d
                ws1.left = w_dd

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

            if(w2 is None):
                L1 = L1 #TODO: delete later




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
            if(w2 is None):
                L1 = L1 #TODO: delete later

        
    else:
        vi_next_inf = inf_coord(vi,vi.right,along_b=True)
        vi_next_inf = Node(0,vi_next_inf[0],vi_next_inf[1])
        if(ccw(vi,vi_next_inf,L1)>0):
            w1 = F1
            w2 = F1.left
            while(w2 is not None):
                if(ccw(vi.right,w1,w2)<0):
                    F1 = w1
                    break
                w1 = w2
                w2 = w2.left
            if(K.head.left is not None): #unbounded
                #case11 with L1
                w1 = L1
                w2 = L1.left
                while(w2 is not None):
                    if(ccw(vi.right,w1,w2)>0):
                        L1 = w1
                        break
                    w1 = w2
                    w2 = w2.left
                if(w2 is None):
                    L1 = L1 #TODO: delete later
            else:
                L1 = L1 #TODO: Remove
        else:
            p = None
            q = None
            wt2 = L1
            wt1 = L1.right
            while(wt2!=F1):
                p = instersection(wt2,wt1,vi,vi_next_inf)
                if(p is not None):
                    w_d = Node(0,p[0],p[1])
                    break
                wt2 = wt1
                wt1 = wt1.right
            if(wt2==F1):
                print("Solution doesn't exist")
                sys.exit(0)
            ws1 = L1
            ws2 = L1.left
            while(ws2 is not None and ws2.left is not None):
                q = instersection(ws1,ws2,vi,vi_next_inf)
                if(q is not None):
                    w_dd = Node(0,q[0],q[1])
                    break
                ws1 = ws2
                ws2 = ws2.left
            if(q is None):
                l_end1=L1
                if(L1.left is not None):
                    l_end2 = L1.left
                else:
                    l_end1 = L1.right
                    l_end2 = L1
                while(l_end2.left is not None):
                    l_end1 = l_end2
                    l_end2 = l_end2.left
                r_end = F1
                while(r_end.right is not None):
                    r_end = r_end.right
                if((ccw(l_end1,l_end2,vi_next_inf)  * ccw(vi,vi_next_inf, r_end)) > 0): #slope is comprised bw the slopes of the two half lines
                    if(wt1.left == K.head):
                        K.head = vi_next_inf
                    wt1.left = w_d
                    w_d.right = wt1
                    w_d.left = vi_next_inf
                    vi_next_inf.right = w_d
                else:
                    head = F1
                    while(head.right is not None):
                        head = head.right
                    wr1 = head
                    wr2 = head.left
                    while(wr2.left is not None):
                        q = instersection(wr1,wr2,vi,vi_next_inf)
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
                    K.head = wr2
    
                    #change Ki
                    #list becomes circular. change head to tail when Ki becomes bounded
            else:
                w_d.left = w_dd
                w_d.right = wt1
                w_dd.right = w_d
                w_dd.left = ws2
                wt1.left = w_d
                ws2.right = w_dd

            #update F1 and L1
            if(is_between(vi,vi.right,w_d)):

                    w1 = F1
                    w2 = F1.left
                    while(w2 is not None):
                        print("here")
                        if(ccw(vi.right,w1,w2)<0):
                            F1 = w1
                            break
                        w1 = w2
                        w2 = w2.left
            else:
                    F1 = w_d
            if(q is None):
                L1 = vi_next_inf
            else:
                if(is_between(vi,vi.right,w_dd)):
                    L1= w_dd
                else:
                    #case (11) with w_dd
                    w1 = w_dd
                    w2 = w_dd.left
                    while(w2 is not None):
                        if(ccw(vi.right,w1,w2)>0):
                            L1 = w1
                            break
                        w1 = w2
                        w2 = w2.left
                    if(w2 is None):
                        L1 = L1 #TODO: delete later
    vi=vi.right
    print("iter %d"%i)
    i+=1

    print("F",F1.x,F1.y)
    print("L",L1.x,L1.y)
    plt.plot(F1.x,F1.y,marker='o', c='k')
    plt.plot(L1.x,L1.y,marker='o', c='b')
    plt.plot(vi.x,vi.y,marker='x',c='r')
    P.plot()
    K.plot()
    plt.show()

P.plot()
K.plot()

plt.show()


"""
use of vector algebra
use of math.isclose to avoid floating point errors.
consistency in variable naming
a single data structure that handles the transformation of a doubly linked list to a circular list.
avoid slope tests, angle tests suggested in the paper with left tests.
"""



"""
a = Node(0,1,2)
b = DoublyLinkedList()
b.append_head(a)
a = Node(2,3,5)
b.append_head(a)
b.delete_node(b.head)

while(b.head is not None):
	print(b.head.v_num)
	b.head = b.head.right


a=Node(0,0,0)
b=Node(1,3,3)
c=Node(2,0,4)
d=Node(3,4,0)
print(instersection(a,b,c,d))
x = [a.x,b.x,c.x,d.x]
y = [a.y,b.y,c.y,d.y]
plt_polygon(x,y)
"""
