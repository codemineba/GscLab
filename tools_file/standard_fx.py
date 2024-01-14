import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import Symbol, sympify, lambdify




def string_to_function(expression):
    if "y" not in expression:
        x = Symbol('x')
        f = sympify(expression)
        f_lambda = lambdify(x, f, 'numpy')
        return f_lambda
    else:
        x = Symbol('x')
        y = Symbol('y')
        f = sympify(expression)
        f_lambda = lambdify((x, y), f, 'numpy')
        return f_lambda




def lagrange(x, y, x_interp):
    fi = 0
    for i in range(len(x)):
        z = 1
        for j in range(len(x)):
            if j is not i:
                z = z * (x_interp - x[j]) / (x[i] - x[j])
        fi = fi + y[i] * z

    return fi



def Newtown(x, y, x_interp):
    chashang = [[0 for i in range(len(x))] for i in range(len(x))]

    for i in range(len(x)):
        if i == 0:
            chashang[i] = y
        else:
            for j in range(len(x) - i):
                chashang[i][j] = (chashang[i-1][j+1] - chashang[i-1][j]) / (x[j+i] - x[j])
    w = 1
    yi = chashang[0][0]
    for j in range(1, len(x)):
        w *= (x_interp - x[j - 1])
        yi += chashang[j][0] * w

    return yi

def Hermite(x, y, dy, x_interp):

    n = len(x)
    m = len(x_interp)
    y_interp = np.zeros(m)

    for j in range(n):
        w = 1
        z = 0
        for k in range(n):
            if k != j:
                w *= (x_interp - x[k]) / (x[j] - x[k])
        for k in range(n):
            if k != j:
                z += 1 / (x[j] - x[k])

        y_interp += (w ** 2) * (y[j] * (1 - 2 * (x_interp - x[j]) * z) + (x_interp - x[j]) * dy[j])

    return y_interp



def Ih(x, y, xi):
    yi = np.zeros(len(xi))
    for i in range(len(xi)):
        for j in range(len(x)):
            if j == 0:
                if x[j] <= xi[i] <= x[j + 1]:
                    lx = (xi[i] - x[j + 1]) / (x[j] - x[j + 1])
                else:
                    lx = 0
            elif j == len(x) - 1:
                if x[j - 1] <= xi[i] <= x[j]:
                    lx = (xi[i] - x[j - 1]) / (x[j] - x[j - 1])
                else:
                    lx = 0
            else:
                if x[j] <= xi[i] <= x[j + 1]:
                    lx = (xi[i] - x[j + 1]) / (x[j] - x[j + 1])
                elif x[j - 1] <= xi[i] <= x[j]:
                    lx = (xi[i] - x[j - 1]) / (x[j] - x[j - 1])
                else:
                    lx = 0
            yi[i] += y[j] * lx

    return yi



def Ihx(x, y,y_, x1):
    Ihx = []
    for j in range(len(x1)):
        yj = 0
        for i in range(len(x)):
            Ax = 1
            Bx = 1
            if i == 0:
                if x[i] <= x1[j]  and x1[j] <= x[i+1]:
                  Ax = (((x1[j] - x[ i +1 ]) / (x[i] - x[ i+1 ])) ** 2) * (1 + 2 * (x1[j] - x[i]) / (x[i+1] - x[i ]))
                  Bx = ((x1[j] - x[ i+1 ]) / (x[i] - x[ i +1 ])) ** 2 * (x1[j] - x[i])
                else :
                  Ax = 0
                  Bx = 0
            elif i == len(x):
                if x[i-1] <= x1[j] and x1[j] <= x[i]:
                    Ax = (((x1[j] - x[i -1 ]) / (x[i] - x[i -1])) ** 2) * (1 + 2 * (x1[j] - x[i]) / (x[i-1] - x[i ]))
                    Bx = (((x1[j] - x[i - 1 ]) / (x[i] - x[i - 1])) ** 2 )* (x1[j] - x[i])
                else :
                    Ax = 0
                    Bx = 0
            else:
                if x[i-1] <= x1[j] and x1[j] <= x[i]:
                  Ax = (((x1[j] - x[i - 1]) / (x[i] - x[i - 1])) ** 2) * (1 + 2 * (x1[j] - x[i]) / (x[i-1] - x[i ]))
                  Bx = ((x1[j] - x[i - 1]) / (x[i] - x[i - 1])) ** 2 * (x1[j] - x[i])
                elif x[i] <= x1[j] and x1[j] <= x[i+1]:
                  Ax = (((x1[j] - x[i + 1]) / (x[i] - x[i + 1])) ** 2) * (1 + 2 * ((x1[j] - x[i]) / (x[i+1] - x[i])))
                  Bx = (((x1[j] - x[i + 1]) / (x[i] - x[i + 1])) ** 2) * (x1[j] - x[i])
                else :
                  Ax = 0
                  Bx = 0
            yj += (y[i]*Ax+y_[i]*Bx)
        Ihx.append(yj)
    return Ihx


def Three_angle(x, y, x1, f01, fn1):
    # 初始化数组
    lower = []
    upper = []
    g = []
    g1 = []
    m = []
    Q = []

    # 添加初始值
    lower.append(0)
    upper.append(0)
    g.append(0)

    # 计算l, u, g
    for i in range(1, len(x)-1):
        lower.append((x[i+1] - x[i]) / (x[i] - x[i-1] + x[i+1] - x[i]))
        upper.append((x[i] - x[i-1]) / (x[i] - x[i-1] + x[i+1] - x[i]))
        g.append(3 * (lower[i] * (y[i] - y[i-1]) / (x[i] - x[i-1]) + upper[i] * (y[i+1] - y[i]) / (x[i+1] - x[i])))

        # 计算g1
        if i == 1:
            g1.append(g[i] - lower[i] * f01)
        elif i == len(x) - 2:
            g1.append(g[i] - upper[i] * fn1)
        else:
            g1.append(g[i])

    # 构造三对角矩阵Q
    for i in range(len(x) - 2):
        t = []
        for j in range(len(x) - 2):
            if j == i - 1:
                t.append(lower[j+1])
            elif j == i:
                t.append(2)
            elif j == i + 1:
                t.append(upper[j+1])
            else:
                t.append(0)
        Q.append(t)

    # 解线性方程组得到系数a
    a = np.linalg.solve(Q, g1)

    # 计算m
    for i in range(len(x)):
        if i == 0:
            m.append(f01)
        elif i == len(x) - 1:
            m.append(fn1)
        else:
            m.append(a[i-1])

    # 计算c
    c = Ihx(x, y, m, x1)
    return c


def Three_moment(x, y, x_vals, f02, fn2):
    u = []
    l = []
    g = []
    g1 = []
    m = []
    Q = []

    # 初始化辅助数组
    l.append(0)
    u.append(0)
    g.append(0)

    # 计算u、l和g数组的值
    for i in range(1, len(x) - 1):
        u.append((x[i + 1] - x[i]) / (x[i] - x[i - 1] + x[i + 1] - x[i]))
        l.append((x[i] - x[i - 1]) / (x[i] - x[i - 1] + x[i + 1] - x[i]))
        g.append(6 * (((y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (y[i] - y[i - 1]) / (x[i] - x[i - 1])) / (
                    x[i] - x[i - 1] + x[i + 1] - x[i])))

        if i == 1:
            g1.append(g[i] - u[i] * f02)
        elif i == len(x) - 2:
            g1.append(g[i] - l[i] * fn2)
        else:
            g1.append(g[i])

    # 构建线性方程组的系数矩阵Q
    for i in range(len(x) - 2):
        t = []
        for j in range(len(x) - 2):
            if j == i - 1:
                t.append(u[j + 1])
            elif j == i:
                t.append(2)
            elif j == i + 1:
                t.append(l[j + 1])
            else:
                t.append(0)
        Q.append(t)

    # 解线性方程组，得到变量a的值
    a = np.linalg.solve(Q, g1)

    # 计算曲线的弯矩值
    for i in range(len(x)):
        if i == 0:
            m.append(f02)
        elif i == len(x) - 1:
            m.append(fn2)
        else:
            m.append(a[i - 1])

    # 对给定的x_vals值进行插值计算
    w_vals = []
    for x_val in x_vals:
        for i in range(len(x) - 1):
            if x_val <= x[i + 1] and x_val >= x[i]:
                w = m[i] * (x[i + 1] - x_val) ** 3 / (6 * (x[i + 1] - x[i])) + \
                    m[i + 1] * (x_val - x[i]) ** 3 / (6 * (x[i + 1] - x[i])) + \
                    (y[i] - m[i] * (x[i + 1] - x[i]) ** 2 / 6) * (x[i + 1] - x_val) / (x[i + 1] - x[i]) + \
                    (y[i + 1] - m[i + 1] * (x[i + 1] - x[i]) ** 2 / 6) * (x_val - x[i]) / (x[i + 1] - x[i])
                break
        w_vals.append(w)

    return w_vals