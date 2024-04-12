import numpy as np
from scipy.spatial import Delaunay

# my array of points
points = [[1,2,3], [2,3,4], [3, 4, 5], []]
# my array of values
values = [7, 8]
# an object with triangulation
tri = Delaunay(points)
# a set of points at which I want to interpolate
p = [[1.5, 2.5, 3.5]]
# this gets simplexes that contain given points
s = tri.find_simplex(p)
print(s)
# this gets vertices for the simplexes
