import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy
from sympy import Symbol, sympify, lambdify

# 指定默认字体为 SimHei
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']


mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.unicode_minus'] = False     # 正常显示图形中的负号



class Gsc_fun_plt:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gsclab10.glade")

        self.window = self.builder.get_object("Gscwindow7")
        self.window.connect("destroy", Gtk.main_quit)

        self.canvas_box = self.builder.get_object("interplt_box")
        self.image_logo = self.builder.get_object("interLogo")
        self.label1 = self.builder.get_object("label1")
        self.label2 = self.builder.get_object('label2')
        self.button1 = self.builder.get_object("button1")
        self.button2 = self.builder.get_object('button2')


        fig = Figure()
        self.canvas = FigureCanvas(fig)
        self.canvas_box.pack_start(self.canvas, True, True, 0)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file("./picture/GscLogo2.png") # 将路径更改为图片的实际路径
        size = 2.1
        smaller_pixbuf = pixbuf.scale_simple(70*size, 45*size, GdkPixbuf.InterpType.BILINEAR)
        self.image_logo.set_from_pixbuf(smaller_pixbuf)



    def run(self):
        self.window.show_all()
        Gtk.main()




if __name__ == "__main__":
    window = Gsc_fun_plt()
    window.run()