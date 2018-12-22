import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint


def __graph(X, Y, Z, s, r, b):
    ax = Axes3D(plt.figure())
    ax.plot(X, Y, Z)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title('Lorenz Attractor $s=' + str(s) + ',r=' + str(r) + ',b=' + str(b) + '$')
    plt.show()


def __lorenz(n, m, s, r, b):
    x, y, z = n
    return s * (y - x), x * (r - z) - y, x * y - b * z


def lorenz1(x0, y0, z0, s=10, r=28, b=2.667):
    n = 10000
    X, Y, Z = [x0], [y0], [z0]
    for _ in range(n):
        x2, y2, z2 = __lorenz((x0, y0, z0), None, s, r, b)
        x1 = x0 + x2 * 0.01
        y1 = y0 + y2 * 0.01
        z1 = z0 + z2 * 0.01
        X.append(x1)
        Y.append(y1)
        Z.append(z1)
        x0, y0, z0 = x1, y1, z1
    __graph(X, Y, Z, s, r, b)


def lorenz2(x0, y0, z0, s=10, r=28, b=2.667):
    n = 10000
    X, Y, Z = np.empty(n), np.empty(n), np.empty(n)
    X[0], Y[0], Z[0] = x0, y0, z0
    for i in range(n - 1):
        x2, y2, z2 = __lorenz((X[i], Y[i], Z[i]), None, s2, r, b)
        X[i + 1] = X[i] + x2 * 0.01
        Y[i + 1] = Y[i] + y2 * 0.01
        Z[i + 1] = Z[i] + z2 * 0.01
    __graph(X, Y, Z, s, r, b)


def lorenz3(x0, y0, z0, s=10, r=28, b=2.667):
    n = 10000
    X, Y, Z = odeint(__lorenz, (x0, y0, z0), np.linspace(0, 100, n), args=(s, r, b)).T
    __graph(X, Y, Z, s, r, b)
