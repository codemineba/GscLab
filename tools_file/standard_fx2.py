import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import Symbol, sympify, lambdify, simplify, expand, N, Poly
from scipy.integrate import quad
import sympy as sp


mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']


mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.unicode_minus'] = False     # 正常显示图形中的负号



def transform_string_fx(string):
    x = Symbol('x')
    if "x" in string:
        temp_f = sympify(string)
        np_f = lambdify(x, temp_f, 'numpy')
    else:
        str_ = sympify(string)
        c = float(str_)
        np_f = lambda x: np.full_like(x, c)
    return np_f


def huajian(fx, xx, n):
    xx = Symbol('x')

    # 使用 Poly 类处理多项式表达式
    poly_fx = Poly(fx, xx)

    # 获取多项式按照幂次从高到低排序后的项
    sorted_terms = poly_fx.terms()
    sorted_terms_temp = sorted_terms

    new_terms = [0 for _ in range(len(sorted_terms))]
    for index, term in enumerate(sorted_terms_temp):
        sorted_terms_temp[index] = list(term)
        new_coefficient = round(float(term[1]), n)
        sorted_terms_temp[index][1] = new_coefficient
        new_terms[index] = new_coefficient

    polynomial = ""
    coefficients = [(c[1], c[0][0]) for c in sorted_terms_temp]
    for coeff, power in coefficients:
        if '-' in str(coeff):
            if power > 1:
                term = f"{abs(coeff)}*x^{power}"
            elif power == 1:
                term = f"{abs(coeff)}*x"
            else:
                term = f"{abs(coeff)}"

            polynomial += " - " + term
        else:
            if power > 1:
                term = f"{abs(coeff)}*x^{power}"
            elif power == 1:
                term = f"{abs(coeff)}*x"
            else:
                term = f"{abs(coeff)}"

            polynomial += " + " + term

    # 处理前三个字符
    if polynomial[:3] == " - ":
        polynomial = "-" + polynomial[3:]
    elif polynomial[:3] == " + ":
        polynomial = polynomial[3:]

    # 去掉化简后的0
    polynomial = expand(polynomial)

    return polynomial


def jifan(f, x1, x2):
    return quad(f, x1, x2)[0]


#################################################
def suqare_(f, x1, x2, n):
    # 普通多项式基的迭代
    n1 = n
    span = ['1']
    for i in range(n1):
        temp = str(expand(span[i] + '* x'))
        span.append(temp)

    # 定义权函数
    px = '1'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):

            span_vertor.append(jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2))
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))

    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span, span_matrix, px


def suqare_Legendre(f, x1, x2, n):
    # Legendre多项式的迭代
    n2 = n
    span = ['1', 'x']
    for i in range(1, n2):
        temp = f'({span[i]} * x * (2 * {i} + 1) - {span[i - 1]} * {i}) / ({i + 1})'
        span.append(temp)
    simplify_exprs = [expand(expr) for expr in span]
    span_Legendre = ['(' + str(expr) + ')' for expr in simplify_exprs]

    # 定义权函数
    px = '1'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            # print((span[i] + '*' + span[j]))
            value = jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2)
            if value < 0.00001:
                value = 0
            span_vertor.append(value)
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span_Legendre, span_matrix, px


def suqare_Chebyshev(f, x1, x2, n):
    # Chebyshev多项式的迭代
    n3 = n
    span = ['1', 'x']
    for i in range(1, n3):
        temp = f'({span[i]} * x * 2 - {span[i - 1]})'
        span.append(temp)
    simplify_exprs = [expand(expr) for expr in span]
    span_Chebyshev = ['(' + str(expr) + ')' for expr in simplify_exprs]

    # 定义权函数
    px = '1 / (1 - x **2) ** (1/2)'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            # print((span[i] + '*' + span[j] + '/ (1 - x **2) ** (1/2)'))
            value = jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2)
            if value < 0.00001:
                value = 0
            span_vertor.append(value)
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span_Chebyshev, span_matrix, px


def suqare_Chebyshev2(f, x1, x2, n):
    # 第二类Chebyshev多项式的迭代
    n4 = n
    span = ['1', '2 * x']
    for i in range(1, n4):
        temp = f'({span[i]} * x * 2 - {span[i - 1]})'
        span.append(temp)
    simplify_exprs = [expand(expr) for expr in span]
    span_Chebyshev2 = ['(' + str(expr) + ')' for expr in simplify_exprs]
    print(span_Chebyshev2)

    # 定义权函数
    px = '(1 - x **2) ** (1/2)'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            # print((span[i] + '*' + span[j] + '* (1 - x **2) ** (1/2)'))
            value = jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2)
            if value < 0.00001:
                value = 0
            span_vertor.append(value)
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span_Chebyshev2, span_matrix, px


def suqare_Laguerre(f, x1, x2, n):
    # Laguerre多项式的迭代
    n5 = n
    span = ['1', '(1 - x)']
    for i in range(1, n5):
        temp = f'({span[i]} * (1 + 2*{i} - x) - {span[i - 1]} * {i}* {i})'
        span.append(temp)
    simplify_exprs = [expand(expr) for expr in span]
    span_Laguerre = ['(' + str(expr) + ')' for expr in simplify_exprs]

    # 定义权函数
    px = 'exp(-x)'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            # print((span[i] + '*' + span[j] + '* exp(-x)'))
            value = jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2)
            if value < 0.00001:
                value = 0
            span_vertor.append(value)
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span_Laguerre, span_matrix, px


def suqare_Hermite(f, x1, x2, n):
    # Hermite多项式
    n6 = n
    span = ['1', '2 * x']
    for i in range(1, n6):
        temp = f'({span[i]} * 2 * x - {span[i - 1]} * 2 * {i})'
        span.append(temp)
    simplify_exprs = [expand(expr) for expr in span]
    span_Hermite = ['(' + str(expr) + ')' for expr in simplify_exprs]

    # 定义权函数
    px = 'exp(-x ** 2)'

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            # print((span[i] + '*' + span[j] + '* exp(- x ** 2)'))
            value = jifan(transform_string_fx((span[i] + '*' + span[j] + '*' + px)), x1, x2)
            if value < 0.00001:
                value = 0
            span_vertor.append(value)
        span_matrix.append(span_vertor)

    f_matrix = []
    for i in range(len(span)):
        f_matrix.append(jifan(transform_string_fx((f + '*' + span[i] + '*' + px)), x1, x2))


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span_Hermite, span_matrix, px

# -----------------------------------------------

def suqare_points(f, x, x1, x2, n):
    # 普通多项式基的迭代
    n1 = n
    span = ['1']
    for i in range(n1):
        temp = span[i] + '* x'
        span.append(temp)

    span_matrix = []
    for i in range(len(span)):
        span_vertor = []
        for j in range(len(span)):
            span_temp = 0
            for k in range(len(x)):
                span_temp += transform_string_fx(span[i])(x[k]) * transform_string_fx(span[j])(x[k])
            span_vertor.append(span_temp)
        span_matrix.append(span_vertor)

    f_matrix = []
    if isinstance(f, str):
        for i in range(len(span)):
            f_temp = 0
            for k in range(len(x)):
                f_temp += transform_string_fx(span[i])(x[k]) * transform_string_fx(f)(x[k])
            f_matrix.append(f_temp)
    else:
        for i in range(len(span)):
            f_temp = 0
            for k in range(len(x)):
                f_temp += transform_string_fx(span[i])(x[k]) * f[k]
            f_matrix.append(f_temp)


    a = np.linalg.solve(span_matrix, f_matrix)

    x_draw = np.linspace(x1, x2, 100)

    y_draw = 0
    for i in range(len(span)):
        y_draw += a[i]*transform_string_fx(span[i])(x_draw)

    return x_draw, y_draw, a, span, f_matrix



# -----------------------------------
def one(fx_str, a, b):

    x = sp.Symbol('x')
    # 将字符串转化为sympy的表达式
    f_sympy = sp.sympify(fx_str)

    # 将字符串转化为numpy的表达式
    f_numpy = lambdify(x, f_sympy, "numpy")

    # 求导(sympy的表达式)
    dfx = sp.diff(f_sympy, x)
    dfx2 = (f_numpy(b) - f_numpy(a)) / (b - a)

    ee = sp.Eq(dfx, dfx2)
    x2 = float(sp.solve(ee, x)[0])

    f_str = f'1/2 * ({f_numpy(a)} + {f_numpy(x2)}) + {dfx2} * (x - ({a} + {x2}) / 2)'

    return f_str


# 生成原函数
def get_yuanfx(a, span):
    # 获取原函数
    fx_str = ''
    for i in range(len(span)):
        if i == 0:
            fx_str += str(a[i]) + ' * ' + span[i]
        else:
            if a[i] < 0:
                fx_str += str(a[i]) + ' * ' + span[i]
            else:
                fx_str += ' + '
                fx_str += str(a[i]) + ' * ' + span[i]
    return fx_str


