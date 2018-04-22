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

    def append_tail(self,node):
        #insert head on the first insert or initialise the list with one element when the list is created.
        temp = self.head
        while(temp.right is not None):
            temp = temp.right
        node.left = temp
        temp.right=node

    def delete_node(self,node):
        if(self.head is None):
            print("empty list")
            return
        #will also be circular list XD Think about cases.
        if self.head==node:
            self.head = self.head.right
        temp = self.head
        while(temp is not None and temp != node):
        	print(temp)
        	temp=temp.right
        if(temp is None):
            print("element not found")
        else:
        	node.left.right = temp.right
        	if node.right is not None:
        		node.right.left = temp.left 

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

