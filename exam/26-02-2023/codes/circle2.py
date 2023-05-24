#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
#sys.path.insert(0,'/sdcard/Download/anusha1/CoordGeo')
sys.path.insert(0,'/sdcard/github/cbse-papers/CoordGeo')         #path to my scripts


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from conics.funcs import inter_pt

#if using termux
import subprocess
import shlex
#end if


#Standard basis vectors
e1 = np.array((1,0)).reshape(2,1)
e2 = np.array((0,1)).reshape(2,1)

#Input parameters
r  = 5
d =10
theta=np.pi/3
#h = np.array((-d,0)).reshape(2,1)
h11=np.sin(theta/2) #*np.array(([mp.cos(theta),mp.sin(theta)]))
h=-r/h11*e1
h = np.array((d,0)).reshape(2,1)
V = np.eye(2)
u = np.zeros((2,1))
f =-r**2
[q11,q12,q21,q22]= inter_pt(h,V,u,f)
k = 2
h1 = (2*q11+h)/3
[p11,p12,p21,p22]= inter_pt(h1,V,u,f)
#S = (V@h+u)@(V@h+u).T-(h.T@V@h+2*u.T@h+f)*V
###Centre and point 
##u = np.array(([0,0]))
O = -u.T
#
##Intermediate parameters
#
#f0 = np.abs(f+u.T@LA.inv(V)@u)
#
##Eigenvalues and eigenvectors
#D_vec,P = LA.eig(S)
#lam1 = D_vec[0]
#lam2 = D_vec[1]
#p1 = P[:,1].reshape(2,1)
#p2 = P[:,0].reshape(2,1)
#D = np.diag(D_vec)
#t1= np.sqrt(np.abs(D_vec))
#negmat = np.block([e1,-e2])
#t2 = negmat@t1
#
##Normal vectors to the conic
#n1 = P@t1
#n2 = P@t2
#print("t1=",t1,"t2=",t2,"p=",P)
##kappa
#den1 = n1.T@LA.inv(V)@n1
#den2 = n2.T@LA.inv(V)@n2
#
#k1 = np.sqrt(f0/(den1))
#k2 = np.sqrt(f0/(den2))
#
#q11 = LA.inv(V)@((k1*n1-u.T).T)
#q12 = LA.inv(V)@((-k1*n1-u.T).T)
#q21 = LA.inv(V)@((k2*n2-u.T).T)
#q22 = LA.inv(V)@((-k2*n2-u.T).T)



#print(q11,q12,q21,q22)

#
##Generating all lines
xhq12 = line_gen(h,q11)
xhq22 = line_gen(h,q21)
xhp21 = line_gen(h1,p21)
#
##Generating the circle
x_circ= circ_gen(O,r)
#
##Plotting all lines
plt.plot(xhq12[0,:],xhq12[1,:],label='$Tangent1$')
plt.plot(xhq22[0,:],xhq22[1,:],label='$Tangent2$')
plt.plot(xhp21[0,:],xhp21[1,:],label='$Tangent2$')
#
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')
#
#
#Labeling the coordinates
#tri_coords = np.vstack((h.T,q11.T,q12.T,q21.T,q22.T,O)).T
tri_coords = np.vstack((h.T,q11.T,q21.T,h1.T,p21.T,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
#vert_labels = ['h','q11','q12','q21','q22','O']
vert_labels = ['C','P','Q','A','R','O']
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
#
#if using termux
#plt.savefig('/sdcard/Download/anusha1/python1/circle2.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/Download/anusha1/python1/circle2.pdf"))
#if using termux
plt.savefig('/sdcard/gitlab/fwc/exam/27-11-2022/figs/circle.pdf')
subprocess.run(shlex.split("termux-open /sdcard/gitlab/fwc/exam/27-11-2022/figs/circle.pdf"))
#else
#plt.show()
#subprocess.run(shlex.split("termux-open /sdcard/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-13.pdf"))
#else
plt.show()
#
#
#
#
#
#
#
