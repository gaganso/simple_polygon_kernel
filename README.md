# simple_polygon_kernel

Course : [Computational Geometry](http://www.ams.sunysb.edu/~jsbm/courses/545/ams545.html)

Professor : [Dr. Joseph Mitchell](http://www.ams.sunysb.edu/~jsbm/)

Implementation of the paper  [An Optimal Algorithm for Finding the Kernel of a Polygon" by Lee and Preparata.](http://delivery.acm.org/10.1145/330000/322142/p415-lee.pdf?ip=130.245.192.20&id=322142&acc=ACTIVE%20SERVICE&key=7777116298C9657D%2E321B0ADB4933783F%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1525573763_ac4cbf8e044c7e661ba7b94fe92818ef)


Requirements:  
Python 3.5.2

Build:
python dll.py -i [num of vertices in the polygon]

Example:
python dll.py -i 9

The user can input any number of vertices of the polygon in counter-clockwise order(This order is imposed by the algorithm since we take the left half-plane of each edge to build the kernel).

Ouput:
Each iteration of the algorithm is displayed to the user with the point of intersection of the supporting lines and the kernel polygon marked in blue and black. The source vertex of the edge under consideration is also displayed with a cross mark in red. The user has to close the window to continue to the next iteration.
