import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd


fig = plt.figure(figsize=(15, 8))
ax1 = fig.add_subplot(111)

x1 = [39.7, 47.8, 55.9, 63.7, 71.6, 79.7, 87.6, 94.9, 103.1, 119.1]
y1 = [200, 240, 280, 320, 360, 400, 440, 480, 520, 600]

x = [39, 120]
y = np.interp(x, x1, y1)

ax1.scatter(x1, y1, marker='x')
ax1.errorbar(x1, y1, yerr=5, xerr=0.6, color='k', linestyle='None')
ax1.plot(x, y, 'r')
ax1.grid()

plt.show()
# задание 1


pos = 30
scale = 10
size = 10000
fig = plt.figure(figsize = (10,20))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

values = np.random.normal(pos, 10, size)
ax1.hist(values, 20)
ax2.hist(values, 100)
ax3.hist(values, 400)
plt.show()
#задание 2



df = pd.read_csv('iris_data.csv')
print(list(df))
mas = list(df['Species'])
s1 = mas.count('Iris-setosa')/150
s2 = mas.count('Iris-versicolor')/150
s3 = mas.count('Iris-virginica')/150
fig = plt.figure(figsize = (7,20))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.pie([s1, s2, s3], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
ax1.set_title('Species')

l1 = l2 = l3 = 0
le = list(df['PetalLengthCm'])
for i in range(len(le)):
    if le[i] < 1.2:
        l1 += 1
    elif le[i] > 1.5:
        l3 += 1
    else:
        l2 += 1
print(l1, l2, l3)
l1 = l1/150
l2 = l2/150
l3 = l3/150

ax2.pie([l1, l2, l3], labels = ['Small','Middle','Large'])
ax2.set_title('Size')
plt.show()
#задача 3



df = pd.read_csv('iris_data.csv')
print(list(df))
mas = list(df)
mas1 = list(df['SepalLengthCm'])
mas2 = list(df['SepalWidthCm'])
mas3 = list(df['PetalLengthCm'])
mas4 = list(df['PetalWidthCm'])
fig, axs = plt.subplots(3, 2, layout='constrained')
axs[0, 0].scatter(mas1, mas2, marker='x')
axs[1, 0].scatter(mas1, mas3, marker='x')
axs[2, 0].scatter(mas1, mas4, marker='x')
axs[0, 1].scatter(mas2, mas3, marker='x')
axs[1, 1].scatter(mas2, mas4, marker='x')
axs[2, 1].scatter(mas3, mas4, marker='x')


plt.show()
# задача 4









'''
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)


x1 = np.array([1.843**2 * 9.3, 1.68**2 * 14, 1.574**2 * 18.5, 1.528**2 * 23, 1.524**2 * 27.5, 1.536**2 * 32, 1.559**2 * 36.5])
y1 = np.array([100, 225, 400, 625, 900, 1225, 1600])


x = [30, 90]
y = np.interp(x, x1, y1)

a, b = np.polyfit(x1, y1, 1, rcond=None)
print(a,b)

plt.plot([30, 60, 90], [30 * a + b, 60 * a + b, 90 * a + b])
ax1.scatter(x1, y1, marker='x')
ax1.errorbar(x1, y1, yerr=20, xerr=0.6, color='k', linestyle='None')
ax1.grid()
plt.savefig('laba.pdf', dpi=300)

plt.show()
'''


'''
fig = plt.figure(figsize=(15, 8))
ax1 = fig.add_subplot(111)


x1 = [10, 15, 20, 25, 30, 35, 40]
y1 = [1.843, 1.68, 1.574, 1.528, 1.524, 1.536, 1.559]

ax1.plot(x1, y1)
ax1.scatter(x1, y1, marker='x')
ax1.grid()
plt.savefig('laba2.pdf', dpi=300)

plt.show()
'''

