import matplotlib.pyplot as plt

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
            self.head.left = node
            node.right = self.head
            self.head = node

    def append_tail(self,node,make_circular=False):
        if(self.head is None):
            self.head = node
            return
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
        #will also be circular list XD Think about cases.
        if self.head==node:
            self.head = self.head.right
        temp = self.head
        while(temp is not None and temp != node):
        	temp=temp.right
        if(temp is None):
            print("element not found")
        else:
        	node.left.right = temp.right
        	if node.right is not None:
        		node.right.left = temp.left
    def plot(self):
        circular = self.head.left is not None
        temp = self.head.right
        x = []
        y = []
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
        v_num = None
        while(temp!= self.head): #reflex test is always for a circular list
            if(ccw(temp.left,temp,temp.right) <0 ):# we will remove all straight edges. degenerate, ignore for now
                v_num = temp.v_num
                print(temp.x,temp.y)
                break
            temp = temp.right
        return v_num


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

#inpt = [(2,1),(5,0),(6,5),(8,8),(7,9),(5.5,13),(4,11),(2,11.5),(3,8.5),(3,6),(0,4)]
inpt = [(1,1),(2,2),(1,3),(0,2)]
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

#remove all straight edges :/
K = DoublyLinkedList()

ref_v = P.first_reflex_node()


if(ref_v is None):
    print("the polygon is convex. It can be gaurded by a single gaurd and the whole of the polygon is its kernel.")





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
