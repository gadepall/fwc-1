import sympy  
from sympy import * 
f = x**2 -2*x-15
g = x**3+27
# Using sympy.gcd() method 
gfg = sympy.gcd(f, g)  
print(gfg)