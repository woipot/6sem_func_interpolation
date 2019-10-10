import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

a = -50000
b = 5
A = 3
p = 2
d = 10


def f(x):
    return A * x * np.sin(-x ** p / d)


N = 101
X = np.linspace(a, b, num=N, endpoint=True)
Y = f(X)

fig1, __ = plt.subplots()
plt.plot(X, Y, '--y')
plt.xlim(a, b)
plt.xlabel("x")
plt.ylabel("y")

Nd = 300
Xd = np.linspace(a, b, num=Nd, endpoint=True)
Yd = f(Xd)
plt.plot(Xd, Yd, 'sb')

f1 = interp1d(Xd, Yd, kind="linear")
Y1 = f1(X)
plt.plot(X, Y1, '-k')
plt.legend(['data', 'linear'], loc='best')
plt.title("linear spline")

f2 = interp1d(Xd, Yd, kind="cubic")
Y2 = f2(X)
fig2, __ = plt.subplots()
plt.plot(X, Y, '--b')
plt.plot(X, Y, '--m')
plt.xlim(a, b)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['data', 'cubic'], loc='best')
plt.title("cubic spline")

esp1 = max(abs(f1(X) - f(X)))
print("linear interpolate: {:.3f}".format(esp1))
esp2 = max(abs(f2(X) - f(X)))
print("cubic interpolate: {:.3f}".format(esp2))
plt.show()
