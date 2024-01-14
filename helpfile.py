import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Gschelp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gschelp.glade")

        self.window = self.builder.get_object("Gsc_help")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)

        vbox = self.builder.get_object("help_box")


        self.window.set_size_request(580, 290)

        text_label = Gtk.Label()
        head = """       使用说明书：科学计算软件
   感谢您选择使用我们的GscLab科学计算软件。
   本使用说明书将向您介绍软件的各项功能及其使用方法。
   以下是软件的主要功能：        
        """
        text_label.set_text(head)
        # 设置靠左对其
        text_label.set_halign(Gtk.Align.START)
        vbox.add(text_label)


        text_expander = Gtk.Expander(
            label="1.计算器功能："
        )
        text_expander.set_expanded(False)
        vbox.add(text_expander)

        msg = """
我们的软件内置了一个强大的计算器，可以帮助您进行各种数值计算。
您可以输入数学表达式，并获得相应的计算结果。
支持基本的四则运算、括号、指数、三角函数等数学运算。

使用方法：

在计算器界面中，使用键盘输入数学表达式。
按下“计算”按钮，即可进行计算。
计算结果将显示在界面上
"""
        details = Gtk.Label(label=msg)
        text_expander.add(details)




        # 在创建下一个 Gtk.Expander 之前添加空行
        vbox.add(Gtk.Label())
        text_expander = Gtk.Expander(
            label="2.绘制函数图像功能："
        )
        text_expander.set_expanded(False)
        vbox.add(text_expander)

        msg = """
我们的软件提供了绘制函数图像的功能，可以帮助您可视化函数的形状和变化趋势。
您可以输入一个函数表达式，并绘制出它的图像

使用方法：

在函数图像绘制界面中，输入或选择函数表达式。
按下“确认”按钮，即可绘制函数图像。绘制的图像将显示在界面上。
"""
        details = Gtk.Label(label=msg)
        text_expander.add(details)



        # 在创建下一个 Gtk.Expander 之前添加空行
        vbox.add(Gtk.Label())
        text_expander = Gtk.Expander(
            label="3.GMSH网格显示功能："
        )
        text_expander.set_expanded(False)
        vbox.add(text_expander)

        msg = """
我们的软件可以用于显示和可视化网格文件。GMSH 是一种常用的网格生成软件，
并广泛应用于有限元分析和计算流体力学等领域。

使用方法：

在菜单栏中选择“文件”>“打开”来加载 GMSH 网格文件。
加载后，网格将在软件界面中显示出来，并可进行缩放和旋转等操作。

也可输入或选择数学函数表达式来绘制出对应的网格图形
"""
        details = Gtk.Label(label=msg)
        text_expander.add(details)



        # 在创建下一个 Gtk.Expander 之前添加空行
        vbox.add(Gtk.Label())
        text_expander = Gtk.Expander(
            label="4.数值分析误差可视化功能："
        )
        text_expander.set_expanded(False)
        vbox.add(text_expander)

        msg = """
我们的软件还提供了数值分析误差的可视化功能，
可以帮助您了解数值计算和数值方法的误差情况。
您可以输入一个数学函数和一个数值方法，然后比较数值结果与精确解的差异。

使用方法：

在数值分析误差可视化界面中，输入或选择要计算的数学函数和数值方法。
按下“绘制”按钮后，软件将计算数值结果和精确解，
并显示误差情况的可视化图象。
        """

        details = Gtk.Label(label=msg)
        text_expander.add(details)

        # 在创建下一个 Gtk.Expander 之前添加空行
        vbox.add(Gtk.Label())

        self.window.show_all()


    def run(self):

        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gschelp()
    app.run()