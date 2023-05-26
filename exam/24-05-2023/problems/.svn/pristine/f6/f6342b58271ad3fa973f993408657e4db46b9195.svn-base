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



A=np.array([7,10])

B=np.array([-2,5])

C=np.array([3,-4])

#checking the right angle
if ((A-C).T@(B-C)==0):
	print("ABC is a right triangle and right angle at c")
elif ((A-B).T@(C-B)==0):
	print("ABC is a right triangle and right angle at B")
elif ((B-A).T@(C-A)==0):
	print("ABC is a right triangle and right angle at A")
else:
	print("ABC is a not right triangle")
if((A-C).T@(B-C)==(A-B).T@(C-B)):
    print("ABC is a isosceles and AC=AB")
elif((B-A).T@(C-A)==(A-B).T@(C-B)):
    print("ABC is a isosceles and BC=AC")
elif((B-A).T@(C-A)==(A-C).T@(B-C)):
    print("ABC is a isosceles and BC=AB")
else:
    print("ABC is a not isosceles triangle")

#
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
#
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB=BC$')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')
plt.plot(x_CA[0,:],x_CA[1,:])#,label='$Diameter$')
#
#
#Labeling the coordinates
tri_coords = np.vstack((A,B,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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