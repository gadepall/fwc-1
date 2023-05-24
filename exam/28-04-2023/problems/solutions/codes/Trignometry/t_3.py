import numpy as np
import matplotlib.pyplot as plt 
import math
db =100
eb = np.pi/6
hg = 20
eg = np.pi/4
h = db*math.tan(eb)
dg = (h-hg)/math.tan(eg)
print(dg)
