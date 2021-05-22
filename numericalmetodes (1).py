# dy/dx=x+y
# y=y0+dy/dx*h
# h=xi-xi-1
import matplotlib.pyplot as plt
import numpy as np

# Inclinação


def f(x, y):
    F = x+y  # dy/dx=x+y
    return F


x0 = 0.0
xn = 10
h = 0.1
n = (xn-x0)/h
x = np.zeros(int(n+1))
y = np.zeros(int(n+1))
xi = np.zeros(int(n+1))
yi = np.zeros(int(n+1))
for i in range(0, int(n)):
    # Valores iniciais
    x[0] = 0
    y[0] = 1
    # Explicit Method
    y[i] = y[i-1]+h*f(x[i-1], y[i-1])
    x[i] = x[i-1]+h
    # Valores iniciais
    xi[0] = 0
    yi[0] = 1
    # Implicit Method
    yi[i] = y[i-1]+h*f(x[i], y[i])
    xi[i] = x[i-1]+h

plt.xlim(0, max(x))
plt.ylim(0, max(y))
plt.plot(x, y, 'ro', label='Explicit Method')
plt.plot(xi, yi, 'b+', label='Implicit Method')
plt.legend()
plt.show()
