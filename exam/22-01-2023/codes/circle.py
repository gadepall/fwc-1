# #Code by GVV Sharma
# November 27, 2022
# #released under GNU GPL
# #Drawing a circle

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# image = mpimg.imread('exit-ramp.jpg')
# plt.imshow(image)
# plt.show()

import sys                                          #for path to external scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts
sys.path.insert(0,'/sdcard/github/cbse-papers/CoordGeo')         #path to my scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/github/training/math/codes/CoordGeo')        #path to my scripts
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import mpmath as mp
from numpy import linalg as LA

#local imports
from line.funcs import *

from triangle.funcs import *
from conics.funcs import circ_gen
from tools.AngleAnnotation import AngleAnnotation


#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if



#def circ_gen(O,r):
#	len = 50
#	theta = np.linspace(0,2*np.pi,len)
#	x_circ = np.zeros((2,len))
#	x_circ[0,:] = r*np.cos(theta)
#	x_circ[1,:] = r*np.sin(theta)
#	x_circ = (x_circ.T + O).T
#	return x_circ
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB

#if using termux
import subprocess
import shlex
#end if

#Input parameters
r = 6
f=-r**2
#O=np.array([0,0])
O=np.array((0,0))
h=np.array((10,0))
#h=np.array([10,0])
#V=np.array([[1,0],[0,1]])
V = np.array(([1,0],[0,1]))
V1=np.linalg.inv(V)
#u=np.array([0,0])
u=np.array((0,0))
#R=np.array([[0,-1],[1,0]])
R = np.array(([0,-1],[1,0]))
#m=np.dot(R,h)
m=R@h
print(R,h,m)
#e1=np.array([1,0])
e1=np.array((1,0))
q=e1/(e1@h)
print(q)
flag = 1

if flag == 0:
    m1 = 1/(m@V@m)
    m2 = (-m@(V@q)+O) + ((np.sqrt((m@(V@q)+O))**2-((q@V@q)+2*O@q+f),(m@V@m)))
    
    m3 = (-m@(V@q)+O) - ((np.sqrt((m@(V@q)+O))**2-((q@V@q)+2*O@q+f),(m@V@m)))
    
    mu1 = m1*m2
    mu2 = m1*m3
    
    print("mu1",mu1)
    print("mu2",mu2)
    
    n1 = q+(mu1*(R@h))
    n2 = q+(mu2*(R@h))
    A = np.dot(V1,(n1-O))
    B = np.dot(V1,(n2-O))
    x = np.linalg.norm(h-A)
    y = np.linalg.norm(h-B)
    #print(x,y)
    #print([math.ceil(x),math.ceil(y)])
    #if(int(x)==int(y)):
    	#print("hA=hB")
    x_hO = line_gen(h,O)
    x_hA = line_gen(h,A)
    x_hB = line_gen(h,B)
    #Generating the circle
    x_circ = circ_gen(O,r)
    plt.plot(x_hO[0,:],x_hO[1,:],label='$10cm$')
    plt.plot(x_hA[0,:],x_hA[1,:],label='$Tangent$')
    plt.plot(x_hB[0,:],x_hB[1,:],label='$Tangent$')
    #plotting the circle
    plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')
    
    #Labeling the coordinates
    tri_coords = np.vstack((O,h,A,B)).T
    plt.scatter(tri_coords[0,:], tri_coords[1,:])
    vert_labels = ['O','h','A','B']
    for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                     (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(5,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc='best')
    plt.grid()
    plt.axis('equal')
    
    #if using termux
    plt.savefig('/sdcard/gitlab/fwc/exam/27-11-2022/figs/circle.pdf')
    subprocess.run(shlex.split("termux-open '/sdcard/gitlab/fwc/exam/27-11-2022/figs/circle.pdf"))
    #else
    #plt.show()
