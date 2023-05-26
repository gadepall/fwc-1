import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/Priyanka/Desktop/courses/pythonandlatex/2007/10/solutions/codes/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

c=5
ang_B=np.pi/3
k1=2
k2=3
B = np.array([0,0])
A = np.array([c*np.cos(ang_B),c*np.sin(ang_B)])
C= np.array([c*np.cos(ang_B),0])
P= np.array([c*np.cos(ang_B),k2])
Q= np.array([k1,0])
if (np.linalg.norm(A-Q)**2+np.linalg.norm(B-P)**2 == np.linalg.norm(A-B)**2+np.linalg.norm(P-Q)**2):
  print(1)
else:
  print(0)
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_AQ = line_gen(Q,A)
x_PB = line_gen(P,B)
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_AQ[0,:],x_AQ[1,:])
plt.plot(x_PB[0,:],x_PB[1,:])
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
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

plt.show()