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

import math
r = 2 
c=np.array([0,0])                           
angle = np.linspace(0, 2*np.pi, 1000) 
x1 = np.cos(angle)*r
y1 = np.sin(angle)*r
plt.plot(x1,y1,label="circle")
d=5
T = np.array([d,0])
A = np.array([0.798,1.834])
B = np.array([1.568,-1.241])
C = np.array([-0.386,-1.962])
D= np.array([0.703,-1.556])



I1=np.linalg.norm(D-T)
I = "{:.1f}".format(I1)
J1 = np.linalg.norm(T-A)
J = "{:.1f}".format(J1)
if (I== J):
  print("Triangle ADT is isosceles")
else:
  print("Triangle ADT is not isosceles")

#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_TC = line_gen(T,C)
x_AT = line_gen(A,T)
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_AD[0,:],x_AD[1,:])
plt.plot(x_TC[0,:],x_TC[1,:],label="Secent")
plt.plot(x_AT[0,:],x_AT[1,:],label="Tangent")
#
#
#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,T)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','T']
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

plt.show()