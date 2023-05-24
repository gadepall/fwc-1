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

b=5
ang_A=np.pi/3
k=2
c=3
A = np.array([0,0])
C = np.array([b*np.cos(ang_A),b*np.sin(ang_A)])
B= np.array([c,0])
E= (1/(k+1))*(k*B+C)
D = (1/(k+1))*(k*A+C)
F= (1/(k+1))*(k*D+C)
X1 = np.linalg.norm(D-C)**2
X = "{:.2f}".format(X1)
Y1 = (np.linalg.norm(C-F)*np.linalg.norm(A-C))
Y = "{:.2f}".format(Y1)
if (X==Y ):
  print(1)
else:
  print(0)
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_BD = line_gen(B,D)
x_EF = line_gen(E,F)
x_DE = line_gen(E,D)
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_BD[0,:],x_BD[1,:])
plt.plot(x_EF[0,:],x_EF[1,:])
plt.plot(x_DE[0,:],x_DE[1,:])
#
#
#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,E,F)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F']
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