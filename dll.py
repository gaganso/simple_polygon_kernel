import matplotlib.pyplot as plt
import math

inf_d = 1000000

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

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        #self.tail=None

    def append_head(self,node):
        if(self.head is None):
            self.head = node
            #self.tail=
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
        temp = self.head.right
        x = [self.head.x]
        y = [self.head.y]
        while temp is not None and temp != self.head:
            x.append(temp.x)
            y.append(temp.y)
            temp=temp.right
        if(circular):
            x.append(x[0])
            y.append(y[0])
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

    def print(self):
        temp = self.head

        print("v_num:%d\t(x,y):(%d,%d)\n"%(temp.v_num,temp.x,temp.y))
        temp = temp.right

        while(temp!=self.head and temp.right is not None):
            print("v_num:%d\t(x,y):(%d,%d)\n"%(temp.v_num,temp.x,temp.y))
            temp = temp.right





def instersection(a,b,c,d):
	r = ((a.y-c.y)*(d.x-c.x)-(a.x-c.x)*(d.y-c.y))/((b.x-a.x)*(d.y-c.y)-(b.y-a.y)*(d.x-c.x))
	s = ((a.y-c.y)*(b.x-a.x)-(a.x-c.x)*(b.y-a.y))/((b.x-a.x)*(d.y-c.y)-(b.y-a.y)*(d.x-c.x))
	if(r >=0 and r<=1 and s>=0 and s<=1):
		return (a.x+r*(b.x-a.x),a.y+r*(b.y-a.y))
	else:
		return None

def ccw(a,b,c):
	return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)


def plt_polygon(x,y):
    plt.plot(x,y)
    plt.show()

def inf_coord(a,b):
    v = (b.x - a.x, b.y - a.y)
    v_mod = math.sqrt(v[0]**2+v[1]**2)
    u = (v[0]/v_mod,v[1]/v_mod)
    return (a.x - inf_d*u[0],a.y - inf_d*u[1])


inpt = [(2,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(4,11),(2,11.5),(3,8.5),(3,6),(0,4)]
#inpt = [(1,1),(2,2),(1,3),(0,2)]
#inpt = [(2,2),(4,4),(2,3),(1,4)]
x = [i[0] for i in inpt]
y = [i[1] for i in inpt]
#plt_polygon(x,y) 

P = DoublyLinkedList()

n = len(inpt)

for i,pt in enumerate(inpt):
    node = Node(i,pt[0],pt[1])
    P.append_tail(node)

#hack to avoid multiple ifs
P.delete_node(node)
P.append_tail(node, make_circular=True)
#P.plot()



P.print()

r_node = P.first_reflex_node()

if(r_node is None):
    print("the polygon is convex. It can be gaurded by a single gaurd and the whole of the polygon is its kernel.")

P.reset_v_num(r_node)
P.print()


K = DoublyLinkedList()

p = inf_coord(r_node,r_node.right) #1st edge. infinity-r_node
q = inf_coord(r_node,r_node.left) #2nd edge. r_node-infinity

print(p,q)
print((p[1]-r_node.y)/(p[0]-r_node.x))
print((r_node.right.y-r_node.y)/(r_node.right.x-r_node.x))

print((q[1]-r_node.y)/(q[0]-r_node.x))
print((r_node.left.y-r_node.y)/(r_node.left.x-r_node.x))

#initialise K1

#point at infinity should be along e1







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
