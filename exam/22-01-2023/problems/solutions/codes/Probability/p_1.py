import matplotlib.pyplot as plt
import numpy as np

y = np.array([600,500,400,700,200])
mylabels = ["VI", "VII", "VIII", "IX","X"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()