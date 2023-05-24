
# #Code by GVV Sharma
# November 13, 2022
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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

#Input parameters
fig, ax = plt.subplots()

fac = np.pi/180
R = 5 #Radius
theta = fac*30
#B = np.zeros((1,2))#Origin

#Vertices
B = np.array((0,0)) #Origin
O = np.array((0,R)) #Centre
A = 2*O #Normal vertex
C = np.array((2*R*np.cos(theta),0)) #Centre

#line parameters
m = A-C
n = omat@m
cn = n@A
#Foot of the perpendicular
P=perp_foot(n,cn,O)
D = 2*P-A

print(O)


##Triangle sides
#a = 6
#b = 5
#c = 4
#
#
##Triangle coordinates
#[A,B,C] = tri_vert(a,b,c)
#
##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OP = line_gen(O,P)
#
##Generating the circumcircle
#[O,R] = ccircle(A,B,C)
x_circ= circ_gen(O,R)

##Generating the incircle
#[I,r] = icircle(A,B,C)
#x_icirc= circ_gen(I,r)
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OP[0,:],x_OP[1,:],label='$OP$')

#Plotting the circumcircle
plt.plot(x_circ[0,:],x_circ[1,:])
#plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')

##Plotting the circumcircle
#plt.plot(x_icirc[0,:],x_icirc[1,:],label='$incircle$')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,P,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','P','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#Plot angle
center = O
p1 = P
p2 = A
#print(p1,p2)
#p1 = 0.5*(O-P)
#p2 = 0.5*(O-A)
am1 = AngleAnnotation(center, p1, p2, ax=ax, size=30, text="$60^{\circ}$", textposition = "outside", text_kw=dict(fontsize=10, xytext = (10,-5)))
#    


#plt.xlabel('$x$')
#plt.ylabel('$y$')
#plt.legend(loc='best')
#plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('tri_sss.pdf')
plt.savefig('/sdcard/gitlab/fwc/exam/figs/circ.pdf')
subprocess.run(shlex.split("termux-open /sdcard/gitlab/fwc/exam/figs/circ.pdf"))

#else
# image = mpimg.imread('tri_sss.png')
# plt.imshow(image)
#plt.show()







