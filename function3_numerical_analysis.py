import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import function3_1_interpolation as f3_1
import function3_2_functionappr as f3_2


def jump_inter(self):
    function3_1 =f3_1.Gsc_inter()
    function3_1.run()

def jump_funcappr(self):
    function3_2 = f3_2.Gsc_functionappr()
    function3_2.run()

class Gsc_funcnum:
    def __init__(self):

        # 创建Gtk.Builder对象并加载Glade文件
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/GscLab8.glade")


        # 获取功能选择界面的窗口
        self.window = self.builder.get_object("Gscwindownum")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)

        # 获取插值法按钮
        self.button1 = self.builder.get_object("buttonnum1")

        # 获取函数逼近的按钮
        self.button2 = self.builder.get_object("buttonnum2")

        # 获取数值积分的按钮
        self.button3 = self.builder.get_object("buttonnum3")

        self.button1.connect("clicked", jump_inter)
        self.button2.connect("clicked", jump_funcappr)

    def run(self):
        # 显示窗口

        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gsc_funcnum()
    app.run()