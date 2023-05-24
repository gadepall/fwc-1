import numpy as np
x=3
y=4
u1 = (x/(x-y))-(y/(x+y))-(2*x*y/(x**2-y**2))
v1 =(x-y)/(x+y)
u = "{:.2f}".format(u1)
v = "{:.2f}".format(v1)
if (u==v):
    print(1)
else:
    print(0)