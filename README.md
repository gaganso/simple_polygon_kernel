# simple_polygon_kernel
The project implements the paper  "An Optimal Algorithm for Finding the Kernel of a Polygon" by Lee and Preparata.

How to run?
python3 dll.py -i [num of vertices in the polygon]

The user can input any number of vertices of the polygon in counter-clockwise order(This order is imposed by the algorithm since we take the left half-plane of each edge to build the kernel).

Ouput:
Each iteration of the algorithm is displayed to the user with the point of intersection of the supporting lines and the kernel polygon marked in blue and black. The source vertex of the edge under consideration is also displayed with a cross mark in red. The user has to close the window to continue to the next iteration.