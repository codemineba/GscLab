import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import function1_plt as f1
import fuction2_gmsh as f2
import function3_numerical_analysis as f3
import function0_calculator as f0
import function4_physics as f4
import function_game as fgame


def jump_calculator(self):
    function0 =f0.Gsc_calculator()
    function0.run()


def jump_plt(self):
    function1 = f1.Gsc_plot()
    # 调用绘图功能类的run方法
    function1.run()


def jump_gmsh(self):
    fuction2 = f2.Gsc_gmsh()
    fuction2.run()


def jump_numer(self):
    fuction3 = f3.Gsc_funcnum()
    fuction3.run()


def jump_games(self):
    fuction_game = fgame.Gsc_game()
    fuction_game.run()


def button_close(widget, win):
    win.destroy()


def jump_physics(self):
    function_phy = f4.Gsc_physics()
    function_phy.run()

class Gsc_func:
    def __init__(self):

        # 创建Gtk.Builder对象并加载Glade文件
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/GscLab2.glade")


        # 获取功能选择界面的窗口
        self.window = self.builder.get_object("Gscwindows2")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)

        # 获取计算器按钮
        self.button0 = self.builder.get_object("Gscbutton_calculator")

        # 获取绘制函数图像功能的按钮
        self.button1 = self.builder.get_object("Gscbutton_plt")

        # 获取绘制gmsh功能的按钮
        self.button2 = self.builder.get_object("Gscbutton_gmsh")

        # 获取数值分析误差可视化的按钮
        self.button3 = self.builder.get_object("Gscbutton_numer")

        # 获取物理模型功能的按钮
        self.button6 = self.builder.get_object("Gscbutton_phy")

        # 获取娱乐按钮
        self.button4 = self.builder.get_object("happybutton")

        # 获取退出按钮
        self.button5 = self.builder.get_object("quitbutton")

        self.button0.connect("clicked", jump_calculator)
        self.button1.connect("clicked", jump_plt)
        self.button2.connect("clicked", jump_gmsh)
        self.button3.connect("clicked", jump_numer)
        self.button4.connect("clicked", jump_games)
        self.button5.connect("clicked", button_close, self.window)
        self.button6.connect("clicked", jump_physics)

        self.image_logo = self.builder.get_object("image2")

        pixbuf = GdkPixbuf.Pixbuf.new_from_file("./picture/GscLogo.png")  # 将路径更改为图片的实际路径

        size = 0.9
        # 调整图片大小
        smaller_pixbuf = pixbuf.scale_simple(131 * size, 90 * size, GdkPixbuf.InterpType.BILINEAR)
        # 将新的缩小图片应用到 Gtk.Image 控件
        self.image_logo.set_from_pixbuf(smaller_pixbuf)


    def run(self):
        # 显示窗口

        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gsc_func()
    app.run()