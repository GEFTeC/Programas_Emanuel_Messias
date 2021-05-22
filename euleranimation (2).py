import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def f(x, y):
    F = x+y
    return F


x0 = 0.0
xn = 10
h = 0.1
n = (xn-x0)/h
x = np.zeros(int(n+1))
y = np.zeros(int(n+1))
xi = np.zeros(int(n+1))
yi = np.zeros(int(n+1))
for i in np.arange(0, int(n+1)):
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
# Criando um Ambiente Figure.
fig = plt.figure()
ax = fig.gca()

# definição de função para animação


def a(i):
    ax.clear()
    ax.plot(x[:i], y[:i], 'b--', label='Explicit Method')
    ax.plot(xi[:i], yi[:i], 'r--', label='Implicit Method')
    ax.legend()

# ax.annotate(round(Ly[i], 2), xy=(Lx[i], Ly[i]))


ani = animation.FuncAnimation(fig, a, range(int(n)))
plt.show()
