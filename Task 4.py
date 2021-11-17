import math
import cmath
import matplotlib.pyplot as plt
import numpy

x = float(input()) #будем считать экспоненту

def exp(x):
    a = 1
    s = 1
    w = x
    for i in range(1, 20):
        s += w/a
        w = w*x
        a = a*(i+1)
    return s
print(exp(x))

y = int(x//1)
if x >=0:
    array = list(range(0,y))
else:
    array = list(range(y,0))

value = list(map(exp, array))

plt.plot(array, value)
plt.show()