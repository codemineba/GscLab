import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import interplt as cha
import tools_file.standard_fx as fx
import numpy as np


from numpy import pi
from numpy import e

# 求导函数
def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)



class Gsc_inter:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gsclab6.glade")

        self.comboBox1 = self.builder.get_object("container1")
        self.comboBox2 = self.builder.get_object("container2")
        self.comboBox3 = self.builder.get_object("container3")
        self.comboBox4 = self.builder.get_object("container4")
        self.comboBox5 = self.builder.get_object("container5")

        self.liststore1 = Gtk.ListStore(str)
        self.liststore1.append(['Lagrange插值'])
        self.liststore1.append(['Newtown插值'])
        self.liststore1.append(['Hermite插值'])
        self.liststore1.append(['分段线性插值'])
        self.liststore1.append(['分段三次Hermite插值'])
        self.liststore1.append(['三转角方程'])
        self.liststore1.append(['三弯矩方程'])
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
        self.liststore3.append(['[1,2,3,4]'])
        self.liststore3.append(['[-5,0,5]'])
        self.liststore3.append(['[-5,-3,-1,1,3,5]'])
        self.liststore3.append(['[-5,-3,-1,0,1,3,5]'])
        self.comboBox3.set_model(self.liststore3)
        self.comboBox3.set_entry_text_column(0)

        self.liststore4 = Gtk.ListStore(str)
        self.liststore4.append(['None'])
        self.comboBox4.set_model(self.liststore4)
        self.comboBox4.set_entry_text_column(0)

        self.liststore5 = Gtk.ListStore(str)
        self.liststore5.append(['None'])
        self.comboBox5.set_model(self.liststore5)
        self.comboBox5.set_entry_text_column(0)

        self.enter1 = self.builder.get_object("enter1")
        self.enter2 = self.builder.get_object("enter2")

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
            self.enter2,
        )

        self.window = self.builder.get_object("Gscwindows6")
        self.window.connect('destroy', Gtk.main_quit)
        self.window.set_resizable(False)



    def turn_to_interplt(self, button, comboBox1, comboBox2, comboBox3, comboBox4, enter1, enter2):
        try:
            # 获取插值信息
            inter_message = comboBox1.get_child().get_text()
            if inter_message == 'Lagrange插值':
                inter_fxx = fx.lagrange
            elif inter_message == 'Newtown插值':
                inter_fxx = fx.Newtown
            elif inter_message == 'Hermite插值':
                inter_fxx = fx.Hermite
            elif inter_message == '分段线性插值':
                inter_fxx = fx.Ih
            elif inter_message == '分段三次Hermite插值':
                inter_fxx = fx.Ihx
            elif inter_message == '三转角方程':
                inter_fxx = fx.Three_angle
            elif inter_message == '三弯矩方程':
                inter_fxx = fx.Three_moment

            # 获取信息
            fxx_string = comboBox2.get_child().get_text()
            # 将文本框中获取的字符型函数转化为numpy的函数
            """转化为numpy的函数的意义在于可以输入np.array,否则只将字符串转化为Sympy的函数只能接受单个值"""
            fxx = fx.string_to_function(fxx_string)

            stringx1 = comboBox3.get_child().get_text()

            list_values1 = eval(stringx1)  # pi 和 e两个常数也能识别

            x_array = np.array(list_values1)
            y_array = fxx(x_array)

            win_plt_inter = cha.Gsc_inter_plt()

            # 设置信息
            # 补充信息
            original_text = win_plt_inter.label1.get_text()
            # 要添加的新文字
            new_text = inter_message
            # 合并文本内容
            combined_text = original_text + new_text
            # 设置合并后的文本内容
            win_plt_inter.label1.set_text(combined_text)

            # 补充信息
            original_text = win_plt_inter.label2.get_text()
            # 要添加的新文字
            new_text = stringx1
            # 合并文本内容
            combined_text = original_text + new_text
            # 设置合并后的文本内容
            win_plt_inter.label2.set_text(combined_text)

            # 绘图
            max_ = np.max(x_array)
            min_ = np.min(x_array)
            # 拟合函数（原函数）的x
            new_x_list = np.linspace(min_, max_, 100)
            new_y_list = []
            # 拟合函数的y
            if (inter_message == 'Lagrange插值' or inter_message == 'Newtown插值' or
                    inter_message == '分段线性插值'):
                new_y_list = inter_fxx(x_array, y_array, new_x_list)

            elif inter_message == '三转角方程' or inter_message == '三弯矩方程':
                # 获取m0和mn:
                m0 = eval(enter1.get_text())
                m1 = eval(enter2.get_text())
                new_y_list = inter_fxx(x_array, y_array, new_x_list, m0, m1)

            elif inter_message == 'Hermite插值' or inter_message == '分段三次Hermite插值':
                # stringx2 = comboBox4.get_child().get_text()
                # list_values2 = eval(stringx2)
                # dy_array = np.array(list_values2)

                dy_array = derivative(fxx, x_array)  # scipy的弃用方法
                # 提取文本框的信息转为sympy函数

                new_y_list = inter_fxx(x_array, y_array, dy_array, new_x_list)

            # 原函数的x
            new_x_list2 = new_x_list
            # 原函数的y
            new_y_list2 = fxx(new_x_list)

            fig = win_plt_inter.canvas.figure
            ax = fig.add_subplot(111)

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
                win_plt_inter.canvas.draw()

            def on_switch_activated1(switch, gparam):
                if switch.get_active():
                    line1.set_visible(True)
                else:
                    line1.set_visible(False)
                win_plt_inter.canvas.draw()

            # 连接函数和"notify::active"信号到switch
            win_plt_inter.button1.connect("notify::active", on_switch_activated2)
            win_plt_inter.button2.connect("notify::active", on_switch_activated1)

            ax.plot(x_array, y_array, color='blue', linestyle='None', marker='o', markersize=5)

            ax.set_xlabel('X')
            ax.set_ylabel('Y')

            title = "实际函数: " + fxx_string
            ax.set_title(title)
            # 添加图例
            ax.legend()

            win_plt_inter.canvas.draw()

            win_plt_inter.run()
            # 每次用完后把删除，防止坐标轴重合
            # fig.delaxes(ax)

        except Exception as e:
            fig.delaxes(ax)
            print(f"Error: {str(e)}")

    def run(self):
        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gsc_inter()
    app.run()
