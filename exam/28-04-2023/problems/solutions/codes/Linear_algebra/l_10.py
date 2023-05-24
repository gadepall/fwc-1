#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts

sys.path.insert(0,'/Users/Priyanka/Desktop/courses/pythonandlatex/2007/10/solutions/codes/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

c=5
a=4
ang_B=np.pi/3
k = 2
B = np.array([0,0])
A = np.array([c*np.cos(ang_B),c*np.sin(ang_B)])
C= np.array([a,0])
P= (1/(k+1))*(k*A+B)
Q = (1/(k+1))*(k*A+C)

#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_PQ = line_gen(P,Q)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_PQ[0,:],x_PQ[1,:])

#
#
#Labeling the coordinates
tri_coords = np.vstack((A,B,C,P,Q)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','P','Q']
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
