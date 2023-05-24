import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/Priyanka/Desktop/courses/pythonandlatex/2007/10/solutions/codes/CoordGeo')        #path to my scripts
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

n= np.array([1,-1])
A= np.array([3,-1])
B= np.array([8,9])
c=2
k= (c-A.T@n)/(B.T@n-c)
print(k)
C= np.array([8,6])
D= np.array([0,-2])
E= np.array([5 ,3])
##Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','E']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
tri_coords = np.vstack((C,D,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['C','D','E']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()


