python_code_gmsh1 = '''
import gmsh
import tools_file.gmsh_tools as tools
import numpy

gmsh.initialize()

# 顶点坐标（二维，形如（x, y））(列表坐标的顺序需要符合首尾相连的顺序)
p = 

# 由给定的顶点坐标生成网格 (p为二维坐标列表)
model1 = tools.model_made_point(p)

gmsh.model.occ.synchronize()  # 同步
gmsh.model.mesh.generate(2)  # 生成网格

gmsh.fltk.run()  # 图形界面显示
gmsh.finalize()  # 关闭gmsh

'''

python_code_gmsh2 = '''
import gmsh
import tools_file.gmsh_tools as tools
import numpy as np
from sympy import Symbol, sympify, lambdify


gmsh.initialize()

# 均匀间隔点的个数
num = 100

string_gx = 

g = tools.string_to_function(string_gx)

# 由给定的极坐标生成网格 (g为极坐标,a ,b 为定义域边界)
model = tools.model_made_polar(g, num)

gmsh.model.occ.synchronize()  # 同步
gmsh.model.mesh.generate(2)  # 生成网格

gmsh.fltk.run()  # 图形界面显示
gmsh.finalize()  # 关闭gmsh

'''


python_code_gmsh3 = '''

import gmsh
import tools_file.gmsh_tools as tools
import numpy as np
from sympy import Symbol, sympify, lambdify

# 均匀间隔点的个数
num = 10

# 定义球坐标 g(x) = 0.2 + 0.05 * (1/8 * (35 * cos(x)^4-30 * cos(x)^2 + 3))

string_gx = 

g = tools.string_to_function(string_gx)

gmsh.initialize()

tools.model_made_globe(g, num)

gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(2)


gmsh.fltk.run()
gmsh.finalize()

'''


python_code_gmsh4 = '''
import gmsh

gmsh.initialize()

gmsh.merge

gmsh.fltk.run()

gmsh.finalize()
'''


def insert_characters(original_str, insert_str, position):
    index = original_str.find(position)
    if index == -1:
        return "原始字符串中找不到 " + insert_str

    position = index + len(position) + 1  # 'p=' 的后面位置

    return original_str[:position] + insert_str + original_str[position:]



def insert_characters_(original_str, insert_str, position):
    index = original_str.find(position)
    if index == -1:
        return "原始字符串中找不到 " + insert_str

    position = index + len(position) + 1  # 'p=' 的后面位置

    return original_str[:position] + "'" + insert_str + "'" +original_str[position:]


def insert_characters__(original_str, insert_str, position):
    index = original_str.find(position)
    if index == -1:
        return "原始字符串中找不到 " + insert_str

    position = index + len(position)   # 'p=' 的后面位置

    return original_str[:position] + " (" + '"' + insert_str + '"' + ")" + original_str[position:]