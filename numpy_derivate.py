import numpy as np
import matplotlib.pyplot as plt
import math



def f(x):
    #return x**2 # y(x) = x^2 -> y'(x) = 2 * x
    return math.tanh(x)


X = np.array ([x for x in range (-10,10,1)])
Y = np.array ([f(x) for x in X])
Yp = np.gradient(Y,X)

plt.figure()
plt.plot (X,Y)
plt.plot (X,Yp, linestyle='dashed')

plt.show()


