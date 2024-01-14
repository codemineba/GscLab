import gi

import time
from functools import partial

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GdkPixbuf
import numpy as np
from numpy import pi
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas,
)
import matplotlib.pyplot as plt


is_paused = True
click_end_times = 0
is_not_end = False
click_pause_times = 0
counter = 0
t3s = []

AA = 4.0
aa = 0.8660254037844386
bb = -0.0

size_x_y = 3/9



def procos1(t, A=AA, a=aa, b=bb):
    return A * np.cos(a * t + b)

def procos2(t, A=AA, a=aa, b=bb):
    return - (A * a * np.sin(a * t + b))


def procos3(t, A=AA, a=aa, b=bb):
    return - (A * a * a * np.cos(a * t + b))


def draw_square(x, y, length, ax):
    # 绘制正方形
    xmin = -AA * 1.75
    xmax = AA * 1.75


    ax.set_xlim(xmin, xmax)
    ax.set_ylim(1, size_x_y *(xmax - xmin))

    rectangle = plt.Rectangle((x, y), length, length, fc='none', ec='black')
    x1 = x
    y1 = y + length/2
    x2 = -AA * 1.75 # y轴
    y2 = y + length/2
    line = ax.plot([x1, x2], [y1, y2], color='black', linewidth=2)[0]

    ax.add_patch(rectangle)

    return rectangle, line


def draw_cos1(t, ax):
    x_ = np.linspace(t, t+4, 100)
    y_ = procos1(x_)
    ax.set_xlim(t, t+4)
    ax.set_ylim(-AA - 0.1, AA + 0.1)

    ax.plot(x_, y_, color='red', linestyle='-', linewidth=1)


    del x_
    del y_

def draw_cos2(t, ax):
    x_ = np.linspace(t, t + 4, 100)
    y_ = procos2(x_)
    ax.set_xlim(t, t + 4)
    ax.set_ylim(-AA*aa - 0.2, AA*aa + 0.2)
    ax.plot(x_, y_, color='blue', linestyle='-', linewidth=1)

    del x_
    del y_


def draw_cos3(t, ax):
    x_ = np.linspace(t, t + 4, 100)
    y_ = procos3(x_)
    ax.set_xlim(t, t + 4)
    ax.set_ylim(-AA*aa*aa - 0.4, AA*aa*aa + 0.4)

    ax.plot(x_, y_, color='black', linestyle='-', linewidth=1)

    del x_
    del y_


def on_pause_button_clicked(self):

    global click_pause_times
    global is_paused
    global is_not_end
    if is_not_end:
        click_pause_times += 1

        if click_pause_times % 2 == 1:
            is_paused = False
        else:
            is_paused = True


def on_timeout(t1, y, length, ax1, ax2, ax3,ax4, canvas1, canvas2, canvas3, canvas4, main_loop):
    canvas1.show()
    canvas2.show()
    canvas3.show()
    canvas4.show()
    if is_paused:
        t2 = time.time()

        if len(t3s) > 0:
            t_zt = t3s[-1] - t3s[0]
            t = t2 - t1 - t_zt
            t3s.clear()
        else:
            t = t2 - t1

        x = procos1(t)
        rec, line = draw_square(x - length/2, y, length, ax1)
        canvas1.draw()


        rec.remove()
        line.remove()

        draw_cos1(t, ax2)
        canvas2.draw()

        draw_cos2(t, ax3)
        canvas3.draw()

        draw_cos3(t, ax4)
        canvas4.draw()
    else:
        print('zt')
        t3 = time.time()
        t3s.append(t3)

    # print(is_not_end)
    if not is_not_end:
        main_loop.quit()
        print('end')

    return is_not_end


def is_end(self, box1, box2, box3, box4):
    global is_not_end
    is_not_end = False

    canvas1 = box1.get_children()
    canvas2 = box2.get_children()
    canvas3 = box3.get_children()
    canvas4 = box4.get_children()

    for child in canvas1:
        if isinstance(child, FigureCanvas):
            box1.remove(child)

    for child in canvas2:
        if isinstance(child, FigureCanvas):
            box2.remove(child)

    for child in canvas3:
        if isinstance(child, FigureCanvas):
            box3.remove(child)

    for child in canvas4:
        if isinstance(child, FigureCanvas):
            box4.remove(child)



def on_button_click(self, box1, box2, box3, box4, switch1, switch2):
    global counter
    print('cccclick')
    if counter % 2 == 0:
        # 调用 plot_function1
        print(counter)
        print('use_fun1')
        plot_function(self, box1, box2, box3, box4, switch1, switch2)
    elif counter % 2 == 1:
        # 调用 plot_function2
        print(counter)
        print('use_fun2')

        is_end(self, box1, box2, box3, box4)
    # 更新计数器
    counter += 1


# 参数 button 是为了接收触发回调函数的信号源，即 confirm_button 按钮。
def plot_function(self, box1, box2, box3, box4, switch1, switch2):

    fig1 = Figure()
    canvas1 = FigureCanvas(fig1)
    box1.pack_start(canvas1, True, True, 0)

    fig2 = Figure()
    canvas2 = FigureCanvas(fig2)
    box2.pack_start(canvas2, True, True, 0)

    fig3 = Figure()
    canvas3 = FigureCanvas(fig3)
    box3.pack_start(canvas3, True, True, 0)

    fig4 = Figure()
    canvas4 = FigureCanvas(fig4)
    box4.pack_start(canvas4, True, True, 0)


    fig1 = canvas1.figure
    fig2 = canvas2.figure
    fig3 = canvas3.figure
    fig4 = canvas4.figure


    ax1 = fig1.add_subplot(1, 1, 1)
    ax2 = fig2.add_subplot(1, 1, 1)
    ax3 = fig3.add_subplot(1, 1, 1)
    ax4 = fig4.add_subplot(1, 1, 1)

    # 设置坐标轴参数
    ax1.set_aspect('equal')
    ax1.yaxis.set_visible(False)


    # ax2.set_aspect('equal')
    ax2.set_xlabel('t', labelpad=-1)
    ax2.set_ylabel('x', labelpad=-1, rotation=0)
    fig2.subplots_adjust(left=0.18, bottom=0.3, right=0.9, top=0.9, wspace=0.2, hspace=0.2)

    # ax3.set_aspect('equal')
    ax3.set_xlabel('t', labelpad=-1)
    ax3.set_ylabel('v', labelpad=-1, rotation=0)
    ax3.autoscale(enable=True, axis='y')
    fig3.subplots_adjust(left=0.18, bottom=0.3, right=0.9, top=0.9, wspace=0.2, hspace=0.2)

    # ax4.set_aspect('equal')
    ax4.set_xlabel('t', labelpad=-1)
    ax4.set_ylabel('a', labelpad=-1, rotation=0)
    fig4.subplots_adjust(left=0.18, bottom=0.3, right=0.9, top=0.9, wspace=0.2, hspace=0.2)

    # 设置其起始时间
    time1 = time.time()

    # 按下按钮后设置为true 循环启动
    global is_not_end
    is_not_end = True

    xmin = -AA * 1.75
    xmax = AA * 1.75

    # 定义箱子长度
    length = 1/3 * size_x_y *  (xmax - xmin)
    # 用红色标记出运动范围（质心)
    line11 = ax1.axvline(x=-AA , color='red', ymin=0, ymax=0.55, linestyle='--')
    line21 = ax1.axvline(x=AA, color='red', ymin=0, ymax=0.55, linestyle='--')
    # 用蓝色标出运动范围 （整体）
    line12 = ax1.axvline(x=-AA - length/2, color='blue', ymin=0, ymax=0.55, linestyle='--')
    line22 = ax1.axvline(x=AA + length/2, color='blue', ymin=0, ymax=0.55, linestyle='--')

    switch1.connect("notify::active", on_switch_activated1, line11, line21, canvas3)
    switch2.connect("notify::active", on_switch_activated2, line12, line22, canvas3)

    main_loop = GLib.MainLoop()
    GLib.timeout_add(90, lambda: on_timeout(time1, 1, length, ax1, ax2, ax3, ax4, canvas1, canvas2, canvas3, canvas4, main_loop))


def on_switch_activated2(switch, gparam, line21,line22, canvas1):
    # switch的状态如果处于 "ON"
    if switch.get_active():
        # 折线可视
        line21.set_visible(True)
        line22.set_visible(True)
    # switch的状态如果处于 "OFF"
    else:
        # 折线不可视
        line21.set_visible(False)
        line22.set_visible(False)
        # 每次调节switch后都要更新状态
    canvas1.draw()

def on_switch_activated1(switch, gparam, line11, line12, canvas1):
    if switch.get_active():
        line11.set_visible(True)
        line12.set_visible(True)
    else:
        line11.set_visible(False)
        line12.set_visible(False)
    canvas1.draw()

# 读取数据的函数
def read_num(self, spin1, spin2, spin3, spin4):
    global aa
    global AA
    global bb
    m = spin1.get_value()
    k = float(spin2.get_value())
    x0 = float(spin3.get_value())
    v0 = float(spin4.get_value())

    # 计算
    aa = (k/m)**(1/2)  # 计算频率
    AA = (x0**2 + v0**2/aa**2)**(1/2)  # 计算振幅
    if x0 ==0:
        bb = 0
    else:
        bb = np.arctan(-v0/(aa * x0))  # 计算初相

    print(aa)
    print(AA)
    print(bb)



def win_quit(self, main_loop):
    main_loop.quit()
    global counter
    counter = 0
    global click_end_times
    click_end_times = 0
    global is_not_end
    is_not_end = False
    global click_pause_times
    click_pause_times = 0
    Gtk.main_quit()


class Gsc_physics(Gtk.Window):

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gscphy.glade")

        self.window = self.builder.get_object("Gsc_phy")
        self.window.connect('destroy', win_quit, GLib.MainLoop())
        self.window.set_resizable(False)

        #  获取可拉的文本框
        self.phycomboBox = self.builder.get_object("phycomboBox")
        self.liststore1 = Gtk.ListStore(str)
        self.liststore1.append(['弹簧振子模型'])
        self.liststore1.append(['单摆模型'])
        self.liststore1.append(['阻尼振荡模型'])
        self.phycomboBox.set_model(self.liststore1)
        self.phycomboBox.set_entry_text_column(0)

        # 获取按钮
        self.button_ok = self.builder.get_object("ok_button")
        self.button_begin_end = self.builder.get_object("begin_end_button")
        self.button_pause = self.builder.get_object("pause_button")


        # 获取绘制图像的ax的box
        self.box_image =  self.builder.get_object("phy_image")


        # 获取绘制函数的ax的box
        self.fun_box1 = self.builder.get_object("phy_function1")
        self.fun_box2 = self.builder.get_object("phy_function2")
        self.fun_box3 = self.builder.get_object("phy_function3")

        self.fig1 = Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.fig2 = Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.fig3 = Figure()
        self.canvas3 = FigureCanvas(self.fig3)
        self.fig4 = Figure()
        self.canvas4 = FigureCanvas(self.fig4)

        # 获取放置参数信息的box
        self.canshuBox = self.builder.get_object("canshubox")

        # 获取不同模型的fixed
        self.temp1win = self.builder.get_object("wintemp1")
        self.tanghuang_fixed = self.builder.get_object("tanghuang_fixed")
        self.temp1win.remove(self.tanghuang_fixed)

        self.temp1win = self.builder.get_object("wintemp2")
        self.dangbai_fixed = self.builder.get_object("dangbai_fixed")
        self.temp1win.remove(self.dangbai_fixed)


        self.canshuBox.pack_start(self.tanghuang_fixed, True, True, 0)
        self.button_ok.grab_focus()

        # 获取switch
        self.switch1 = self.builder.get_object("physwitch1")
        self.switch2 = self.builder.get_object("physwitch2")

        # 获取spin
        self.spin1 = self.builder.get_object("spin1")
        self.spin2 = self.builder.get_object("spin2")
        self.spin3 = self.builder.get_object("spin3")
        self.spin4 = self.builder.get_object("spin4")

        # 设置spinbutton参数
        adjustment1 = self.spin1.get_adjustment()
        adjustment1.set_value(10)
        adjustment1.set_lower(0)  # 下界
        adjustment1.set_upper(100)  # 上界
        adjustment1.set_step_increment(1)  # 步长

        # 设置spinbutton参数
        adjustment2 = self.spin2.get_adjustment()
        adjustment1.set_value(0)
        adjustment2.set_lower(0)  # 下界
        adjustment2.set_upper(100)  # 上界
        adjustment2.set_step_increment(1)  # 步长

        # 设置spinbutton参数
        adjustment3 = self.spin3.get_adjustment()
        adjustment1.set_value(0)
        adjustment3.set_lower(0)  # 下界
        adjustment3.set_upper(100)  # 上界
        adjustment3.set_step_increment(1)  # 步长

        # 设置spinbutton参数
        adjustment4 = self.spin4.get_adjustment()
        adjustment1.set_value(0)
        adjustment4.set_lower(0)  # 下界
        adjustment4.set_upper(100)  # 上界
        adjustment4.set_step_increment(1)  # 步长

        # 获取logo位置
        self.phylogo = self.builder.get_object("gscphyimage")
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("./picture/GscLogo.png")  # 将路径更改为图片的实际路径

        size = 0.9
        # 调整图片大小
        smaller_pixbuf = pixbuf.scale_simple(131 * size, 90 * size, GdkPixbuf.InterpType.BILINEAR)
        # 将新的缩小图片应用到 Gtk.Image 控件
        self.phylogo.set_from_pixbuf(smaller_pixbuf)


        self.button_begin_end.connect("clicked",
                                      on_button_click,
                                      self.box_image,
                                      self.fun_box1,
                                      self.fun_box2,
                                      self.fun_box3,
                                      self.switch1,
                                      self.switch2)

        self.button_ok.connect("clicked", read_num, self.spin1, self.spin2, self.spin3, self.spin4)
        self.button_pause.connect("clicked", on_pause_button_clicked)

    def run(self):
        self.window.show_all()
        Gtk.main()



if __name__ == "__main__":
    app = Gsc_physics()
    app.run()