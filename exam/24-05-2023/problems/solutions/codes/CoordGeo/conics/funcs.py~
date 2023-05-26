#Code by GVV Sharma
#December 7, 2019
#Revised July 15, 2020
#Revised March 4, 2022
#released under GNU GPL
#Functions related to conics

import numpy as np
from params import *

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating points on a circular arc
def circ_arc(O,r,theta1,theta2,len):
	theta = np.linspace(theta1,theta2,len)*np.pi/180
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
#Generating points on an ellipse
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#Generating points on a parabola
def parab_gen(y,a):
	x = y**2/a
	return x

#Generating points on a standard hyperbola 
def hyper_gen(y):
	x = np.sqrt(1+y**2)
	return x

def conic_quad(q,V,u,f):
	return q@V@q + 2*u@q + f

#Points of intersection of a conic section with a line
def inter_pt(m,q,V,u,f):
    a = m@V@m
    b = m@(V@q+u)
    c = conic_quad(q,V,u,f)
    l1,l2 =np.roots([a,2*b,c]) 
#    print(a,b,c)
    x1 = q+l1*m
    x2 = q+l2*m
    return x1,x2 
