from scipy.interpolate import *

x = [0, 5, 8]
y = [6, 2, 15]

p = lagrange(x, y)
print(p)

