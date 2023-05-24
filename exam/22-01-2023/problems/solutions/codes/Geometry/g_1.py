import numpy as np
import matplotlib.pyplot as plt
r =7
ht =31
h = ht-r
l = np.sqrt(h**2+r**2)
s = 2*np.pi*r**2 + np.pi*r*l
print(s)
