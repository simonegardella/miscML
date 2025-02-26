import random
import math
import matplotlib.pyplot as plt
import numpy as np


x = [random.random()*2+2 for i in range  (25)]
y = [random.random()*2+2  for i in range  (25)]
x1 = [random.random()*2 for i in range  (25)]
y1 = [random.random()*2+2 for i in range  (25)]

x3 = [random.random()*2 for i in range  (25)]
y3 = [random.random()*2  for i in range  (25)]
x4 = [random.random()*2+2 for i in range  (25)]
y4 = [random.random()*2 for i in range  (25)]

for i in range (len (x3)):
    x.append(x3[i])
    y.append(y3[i])
    
for i in range (len (x4)):
    x1.append(x4[i])
    y1.append(y4[i])

plt.figure()
plt.scatter(x,y)
plt.scatter(x1,y1)
#plt.show()

k = 2000
p = 1000

x = np.random.random ((k)) * 10
y = np.random.random ((k)) * 20 
z = np.random.random ((k)) * 50


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter (x[:1000],y[:1000],z[:1000],c='r')
ax.scatter (x[1000:],y[1000:],z[1000:],c='g')

plt.show()
    





