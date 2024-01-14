import gmsh
import math
import numpy as np
from sympy import sympify, Symbol, sqrt, Matrix
from sympy.utilities.lambdify import lambdify

# 网格尺寸值
lc = 2e-1


# 用顶点坐标生成网格


# p: 二维顶点坐标组成的列表
def model_made_point(p):
    # 创建点
    points = [gmsh.model.occ.addPoint(*pt, 0, lc) for pt in p]
    # 将点按顺序依次连接，创建线（形成闭合图形）
    lines = [gmsh.model.occ.addLine(points[i-1], points[i]) for i in range(len(points))]
    # 创建线环
    cloop = gmsh.model.occ.addCurveLoop(lines)
    # 创建面
    face = gmsh.model.occ.addPlaneSurface([cloop])

    gmsh.model.occ.synchronize()  # 同步
    gmsh.model.mesh.generate(2)  # 生成网格

    return face


# p: 三维顶点坐标组成的列表
def model_made_points(p, pindex):
    # 创建点
    points = [gmsh.model.occ.addPoint(*pt, lc) for pt in p]
    # 创建边
    lines = [[gmsh.model.occ.addLine(points[pindex[i][j-1]], points[pindex[i][j]]) for j in range(len(pindex[i]))]
             for i in range(len(pindex))]
    # 创建线环
    cloops = [gmsh.model.occ.addCurveLoop(lines[i]) for i in range(len(lines))]
    # 创建面
    faces = [gmsh.model.occ.addPlaneSurface([cloops[i]]) for i in range(len(cloops))]


    # 创建面环
    # surface_loop = gmsh.model.occ.addSurfaceLoop(faces)
    # 创建体
    # volume = gmsh.model.occ.addVolume([surface_loop])
    # return volume


# 用极坐标生成网格

# g: 极坐标方程的函数
# a, b: theta的左右边界(默认为[0, 2*pi])
# num: 均匀间隔点的个数
def model_made_polar(g, num, a=0, b=2 * math.pi):
    # 计算定义域范围内的x坐标和y坐标的值
    theta = np.linspace(a, b, num)

    p = g(theta)
    x = np.cos(theta) * p
    y = np.sin(theta) * p

    # 创建点
    points = [gmsh.model.occ.addPoint(x[i], y[i], 0) for i in range(len(x))]
    # 将点按顺序依次连接，创建线（形成闭合图形）
    lines = [gmsh.model.occ.addLine(points[i], points[i + 1]) for i in range(len(points) - 1)]
    # 创建线环
    cloop = gmsh.model.occ.addCurveLoop(lines)
    # 创建面
    face = gmsh.model.occ.addPlaneSurface([cloop])


    return face


# 用参数方程生成网格

# f: 参数方程函数
# a, b: 参数的左右边界
# num: 均匀间隔点的个数
def model_made_parameter(f, num,  a, b):
    # 计算定义域范围内的x坐标和y坐标的值
    t = np.linspace(a, b, num)
    x, y = f(t)

    # 创建点
    points = [gmsh.model.occ.addPoint(x[i], y[i], 0) for i in range(len(x))]
    # 将点按顺序依次连接，创建线（形成闭合图形）
    lines = [gmsh.model.occ.addLine(points[i], points[i + 1]) for i in range(len(points) - 1)]
    # 创建线环
    cloop = gmsh.model.occ.addCurveLoop(lines)
    # 创建面
    face = gmsh.model.occ.addPlaneSurface([cloop])

    return face


# 用球坐标生成网格

# h: 球坐标方程函数
# a, b: theta的左右边界(默认为[0, 2*pi])
# c, d: phi的左右边界(默认为[0, pi])
# num: 均匀间隔点的个数
def model_made_globe(h, num, a=0, b=2 * math.pi, c=0, d=math.pi):
    # 计算定义域范围内的x坐标、y坐标和z坐标的值
    multiplier = num
    theta = np.linspace(a, b, num)
    phi = np.linspace(c, d, num)
    r = h(theta, phi)
    op = r * np.sin(phi)
    x = [np.cos(a) * b for a in theta for b in op]
    y = [np.sin(a) * b for a in theta for b in op]
    temp = r * np.cos(phi)
    z = []
    for _ in range(multiplier):
        z.extend(temp)

    # 创建点
    points = [gmsh.model.occ.addPoint(x[i], y[i], z[i]) for i in range(len(x))]
    # 将点按顺序依次连接，创建线
    lines1 = [gmsh.model.occ.addLine(points[num * i + j], points[num * i + j + 1])
              for i in range(len(theta)) for j in range(len(phi) - 1)]
    lines2 = [gmsh.model.occ.addLine(points[num * i + j], points[num * (i + 1) + j])
              for j in range(1, len(theta) - 1) for i in range(len(phi) - 1)]
    # 创建线环
    cloops1 = [gmsh.model.occ.addCurveLoop([lines1[(num - 1) * i + j], -lines1[(num - 1) * (i + 1) + j],
               lines2[i]]) for j in [0] for i in range(num - 1)]
    cloops2 = [gmsh.model.occ.addCurveLoop([-lines1[(num - 1) * i + j], lines1[(num - 1) * (i + 1) + j],
               lines2[i + (num - 1) * (num - 3)]]) for j in [num - 2] for i in range(num - 1)]
    cloops3 = [gmsh.model.occ.addCurveLoop([lines1[i + j * (num - 1)], -lines2[(i - 1) * (num - 1) + j + (num - 1)],
               -lines1[i + (j + 1) * (num - 1)], lines2[(i - 1) * (num - 1) + j]])
               for i in range(1, num - 2) for j in range(num - 1)]
    # 创建面
    cloops = cloops1 + cloops3 + cloops2
    face = [gmsh.model.occ.addPlaneSurface([cloops[i]]) for i in range(len(cloops))]
    # 创建面环
    surface_loop = gmsh.model.occ.addSurfaceLoop(face)
    # 创建体
    volume = gmsh.model.occ.addVolume([surface_loop])

    return volume




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