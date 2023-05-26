import numpy as np
import matplotlib.pyplot as plt 
import math
t = np.pi/3
A1 = (math.cos(t)/(1-math.tan(t)))+((math.sin(t)*math.tan(t))/(math.tan(t)-1))
A = "{:.2f}".format(A1)
B1= math.cos(t)+math.sin(t)
B = "{:.2f}".format(B1)
if(A==B):
    print(1)
else:
    print(0)