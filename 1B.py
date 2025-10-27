import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd


fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)


x1 = np.array([0, 12.25, 25, 36, 49, 64])
y1 = np.array([6.3, 7.5, 8.7, 9.6, 10.8, 12.4])


x = [0, 70]
y = np.interp(x, x1, y1)

a, b = np.polyfit(x1, y1, 1, rcond=None)
print(a,b)

plt.plot([-5, 65], [-5 * a + b, 65 * a + b])
ax1.scatter(x1, y1, marker='+')
ax1.errorbar(x1, y1, yerr=0.1, xerr=0.8, color='k', linestyle='None')
ax1.grid()
plt.savefig('laba.pdf', dpi=300)

plt.show()


