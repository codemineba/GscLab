import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import funplt as cha
import tools_file.standard_fx2 as fx2
import numpy as np

from numpy import pi
from numpy import e


class Gsc_functionappr:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gsclab9.glade")

        self.comboBox1 = self.builder.get_object("container1")
        self.comboBox2 = self.builder.get_object("container2")
        self.comboBox3 = self.builder.get_object("container3")
        self.comboBox4 = self.builder.get_object("container4")

        self.liststore1 = Gtk.ListStore(str)
        self.liststore1.append(['最佳一次逼近'])
        self.liststore1.append(['最佳平方逼近'])
        self.liststore1.append(['最小二乘法'])
        self.comboBox1.set_model(self.liststore1)
        self.comboBox1.set_entry_text_column(0)

        self.liststore2 = Gtk.ListStore(str)
        self.liststore2.append(['exp(x)'])
        self.liststore2.append(['sin(x)'])
        self.liststore2.append(['1/(1 + x**2)'])
        self.liststore2.append(['exp(x) + x**4 + x + 100 * sin(x)'])
        self.comboBox2.set_model(self.liststore2)
        self.comboBox2.set_entry_text_column(0)

        self.liststore3 = Gtk.ListStore(str)
        self.liststore3.append(['普通多项式'])
        self.liststore3.append(['Legendre多项式'])
        self.liststore3.append(['Chebyshev多项式'])
        self.liststore3.append(['第二类Chebyshev多项式'])
        self.liststore3.append(['Laguerre多项式'])
        self.liststore3.append(['Hermite多项式'])
        self.comboBox3.set_model(self.liststore3)
        self.comboBox3.set_entry_text_column(0)

        self.liststore4 = Gtk.ListStore(str)
        self.liststore4.append(['[-1 + 10e-10, 1 - 10e-10]'])
        self.liststore4.append(['[0, 100]'])
        self.liststore4.append(['[-100, 100]'])
        self.liststore4.append(['[-3, -2, -1, 0, 1, 2, 3]'])
        self.comboBox4.set_model(self.liststore4)
        self.comboBox4.set_entry_text_column(0)

        self.enter1 = self.builder.get_object("enter1")

        self.matrixlabel = self.builder.get_object("matrixlabel")
        self.jifxlabel = self.builder.get_object("jifxlabel")


        self.button = self.builder.get_object("turntoplt")
        self.button.grab_focus()

        self.button.connect(
            "clicked",
            self.turn_to_interplt,
            self.comboBox1,
            self.comboBox2,
            self.comboBox3,
            self.comboBox4,
            self.enter1,
            self.jifxlabel,
            self.matrixlabel
        )

        self.window = self.builder.get_object("Gscwindows6")
        self.window.connect('destroy', Gtk.main_quit)
        self.window.set_resizable(False)



    def turn_to_interplt(self, button, comboBox1, comboBox2, comboBox3, comboBox4, enter1, jifxlabel, matrixlabel):
        # 获算法信息
        fun_message1 = comboBox1.get_child().get_text()
        fun_message2 = comboBox3.get_child().get_text()
        if fun_message1 == '最佳一次逼近':
            fun_fxx = fx2.one
        elif fun_message1 == '最佳平方逼近':
            if fun_message2 == "普通多项式":
                fun_fxx = fx2.suqare_
                tmp_message = fun_message2
            elif fun_message2 == "Legendre多项式":
                fun_fxx = fx2.suqare_Legendre
                tmp_message = fun_message2
            elif fun_message2 == "Chebyshev多项式":
                fun_fxx = fx2.suqare_Chebyshev
                tmp_message = fun_message2
            elif fun_message2 == "第二类Chebyshev多项式":
                fun_fxx = fx2.suqare_Chebyshev2
                tmp_message = fun_message2
            elif fun_message2 == "Laguerre多项式":
                fun_fxx = fx2.suqare_Laguerre
                tmp_message = fun_message2
            elif fun_message2 == "Hermite多项式":
                fun_fxx = fx2.suqare_Hermite
                tmp_message = fun_message2
        elif fun_message1 == '最小二乘法':
            fun_fxx = fx2.suqare_points

        # 获取信息
        fxx_string = comboBox2.get_child().get_text()
        # 将文本框中获取的字符型函数转化为numpy的函数
        """转化为numpy的函数的意义在于可以输入np.array,否则只将字符串转化为Sympy的函数只能接受单个值"""
        fxx = fx2.transform_string_fx(fxx_string)

        # 基函数的维度
        dim = eval(enter1.get_text())

        # 将信息转化为列表
        stringx = comboBox4.get_child().get_text()
        list_values1 = eval(stringx)  # pi 和 e两个常数也能识别

        listmax = max(list_values1)
        listmin = min(list_values1)

        new_x_list = np.linspace(listmin, listmax, 100)

        if (fun_message1 == '最佳一次逼近'):
            # 得到拟合函数表达式
            fx_str = fun_fxx(fxx_string, listmin, listmax)

            fxx_string_nihe = fx_str
            new_text1 = fun_message1
            new_text2 = '无'
            new_matrix = '无'
            new_span = '无'
            new_y_list = fx2.transform_string_fx(fx_str)(new_x_list)

        elif fun_message1 == '最佳平方逼近':
            x_array, y_array, a, span, matrix, px = fun_fxx(fxx_string, listmin, listmax, dim-1)

            fxx_string_nihe = fx2.get_yuanfx(a, span)
            fxx_string_nihe = fx2.huajian(fxx_string_nihe, 'x', 5)  # 5是化简系数的小数位数
            new_x_list = x_array
            new_y_list = y_array
            new_text1 = fun_message1 + ' ' + tmp_message
            new_text2 = px
            new_matrix = matrix
            new_span = span


        elif fun_message1 == '最小二乘法':

            x_array, y_array, a, span, matrix= fun_fxx(fxx_string, list_values1, listmin, listmax, dim)
            # 提取文本框的信息转为sympy函数

            fxx_string_nihe = fx2.get_yuanfx(a, span)
            fxx_string_nihe = fx2.huajian(fxx_string_nihe, 'x', dim)  # 5是化简系数的小数位数
            new_x_list = x_array
            new_y_list = y_array
            new_text1 = fun_message1
            new_text2 = '无'
            new_matrix = matrix
            new_span = span
            points_x = np.array([list_values1])
            points_y = fx2.transform_string_fx(fxx_string)(points_x)

        win_fun_plt = cha.Gsc_fun_plt()

        # 设置信息
        # 补充信息
        original_text = win_fun_plt.label1.get_text()
        # 合并文本内容
        combined_text = original_text + new_text1
        # 设置合并后的文本内容
        win_fun_plt.label1.set_text(combined_text)

        # 补充信息
        original_text = win_fun_plt.label2.get_text()
        combined_text = original_text + new_text2
        # 设置合并后的文本内容
        win_fun_plt.label2.set_text(combined_text)

        # 填充基和矩阵
        if new_span is not "无":
            jifxlabel.set_text('\n'.join(str(x) for x in new_span))
        if new_matrix is not "无":
            matrixlabel.set_text('\n'.join(str(x) for x in new_matrix))

        # 绘图

        # 原函数的x
        new_x_list2 = new_x_list
        # 原函数的y
        new_y_list2 = fxx(new_x_list)

        fig = win_fun_plt.canvas.figure
        ax = fig.add_subplot(111)

        # 最小二乘法的特殊情况
        if fun_message1 == '最小二乘法':
            ax.plot(points_x, points_y, color='blue', linestyle='None', marker='o', markersize=5)
        # 通过解包操作获取绘制的折线对象
        line1, = ax.plot(new_x_list, new_y_list, color='red', linestyle='-', label='拟合函数')
        line2, = ax.plot(new_x_list2, new_y_list2, color='black', linestyle='--', label='实际函数')

        # 定义调节switch后的信号函数 （switch的函数需要设置两个参数，但第二个参数无实际意义）
        def on_switch_activated2(switch, gparam):
            # switch的状态如果处于 "ON"
            if switch.get_active():
                # 折线可视
                line2.set_visible(True)
            # switch的状态如果处于 "OFF"
            else:
                # 折线不可视
                line2.set_visible(False)
            # 每次调节switch后都要关系状态
            win_fun_plt.canvas.draw()

        def on_switch_activated1(switch, gparam):
            if switch.get_active():
                line1.set_visible(True)
            else:
                line1.set_visible(False)
            win_fun_plt.canvas.draw()

        # 连接函数和"notify::active"信号到switch
        win_fun_plt.button1.connect("notify::active", on_switch_activated2)
        win_fun_plt.button2.connect("notify::active", on_switch_activated1)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        title = "拟合函数: " + str(fxx_string_nihe)
        ax.set_title(title)
        # 添加图例
        ax.legend()

        win_fun_plt.canvas.draw()

        win_fun_plt.run()
        # 每次用完后把删除，防止坐标轴重合
        # fig.delaxes(ax)


    def run(self):
        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gsc_functionappr()
    app.run()
