import matplotlib.pyplot as plt
import numpy as np
import cmath
# Creating vectors X and Y
x = np.linspace(-40, 50, 100)
y = x**2-10*x-1200
a = 1
b = -10
c = -1200

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
A= np.array([sol1,0])
B= np.array([sol2,0])
fig = plt.figure(figsize = (10, 5))
plt.scatter(A[0],A[1],marker="o")
plt.scatter(B[0],B[1],marker="o")
plt.text(A[0],A[1], "A", color='black')
plt.text(B[0],B[1], "B", color='black')
# Create the plot
plt.plot(x, y)
# Show the plot
plt.grid()
plt.show()