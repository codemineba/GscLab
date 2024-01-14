import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess

import tools_file.gmshtxt as gmshtxt
import os


class Gsc_gmsh:
    def __init__(self):


        self.anotherpython = r'C:\Users\27966\AppData\Local\Programs\Python\Python311\python.exe'

        self.selected_file = None  # 增加一个成员变量，用于存储所选文件的路径
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/GscLab4.glade")

        self.window = self.builder.get_object("Gscwindows4")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)

        self.comboBoxContainer1 = self.builder.get_object("container1")
        self.comboBoxContainer2 = self.builder.get_object("container2")
        self.comboBoxContainer3 = self.builder.get_object("container3")

        self.gmshbutton1 = self.builder.get_object("gmshbutton1")
        self.gmshbutton2 = self.builder.get_object("gmshbutton2")
        self.gmshbutton3 = self.builder.get_object("gmshbutton3")


        self.comboBox1 = Gtk.ComboBox.new_with_entry()
        entry = self.comboBox1.get_child()  # 获取文本输入框
        entry.set_placeholder_text("请输入二维顶点坐标（顺序）")
        self.comboBox2 = Gtk.ComboBox.new_with_entry()
        entry = self.comboBox2.get_child()
        entry.set_placeholder_text("请输入极坐标方程")
        self.comboBox3 = Gtk.ComboBox.new_with_entry()
        entry = self.comboBox3.get_child()
        entry.set_placeholder_text("请输入球坐标方程")

        self.gmshbutton1.connect("clicked", self.gmshbutton1_run, self.comboBox1)
        self.gmshbutton2.connect("clicked", self.gmshbutton2_run, self.comboBox2)
        self.gmshbutton3.connect("clicked", self.gmshbutton3_run, self.comboBox3)

        self.liststore1 = Gtk.ListStore(str)
        self.liststore1.append(['[[4, 7], [5, 5], [7, 5], [5, 3.5], [6, 1.5],[4, 2.5], [2, 1.5], [3, 3.5], [1, 5], [3, 5]]'])

        self.liststore2 = Gtk.ListStore(str)
        self.liststore2.append(['0.7 * (1 - sin(x))'])
        self.liststore2.append(['1.0 + 0.2 * sin(5*x)'])
        self.liststore2.append(['0.2 * sin(10 * x)'])

        self.liststore3 = Gtk.ListStore(str)
        self.liststore3.append(['2'])
        self.liststore3.append(['0.2 + 0.05 * (1/8 * (35 * cos(x)**4-30 * cos(x)**2 + 3))'])
        self.liststore3.append(['sin(x) * cos(y)'])
        self.liststore3.append(['x**2 + y**2'])
        self.liststore3.append(['exp(sin(x)) - cos(y)**3 * sin(5*x)'])
        self.liststore3.append(['1.5 + 0.8 * (1/8 * (2 * cos(x)**4 - cos(x)**2 + 0.5) * (1.5 * cos(y)**4 - 0.7 * cos(y)**2 + 1))'])
        self.liststore3.append(['sin(2*x) * cos(3*y) + exp(cos(x)) * sin(y)'])

        self.comboBox1.set_model(self.liststore1)
        self.comboBox2.set_model(self.liststore2)
        self.comboBox3.set_model(self.liststore3)

        # 将 Gtk.ComboBox 添加到容器中
        self.comboBoxContainer1.pack_start(self.comboBox1, True, True, 0)
        self.comboBoxContainer2.pack_start(self.comboBox2, True, True, 0)
        self.comboBoxContainer3.pack_start(self.comboBox3, True, True, 0)

        self.comboBox1.set_entry_text_column(0)
        self.comboBox2.set_entry_text_column(0)
        self.comboBox3.set_entry_text_column(0)

        self.file_chooser = self.builder.get_object("file_open")  # 获取GtkFileChooserButton对象
        self.file_chooser.connect("file-set", self.on_file_set)  # 连接"file-set"信号

        self.ok_button = self.builder.get_object("okbutton")
        self.ok_button.connect("clicked", self.ok_gmsh_show)


    def on_file_set(self, widget):
        self.selected_file = self.file_chooser.get_filename()  # 获取选定文件的路径


    def run(self):
        self.window.show_all()
        Gtk.main()


    def ok_gmsh_show(self, widget):
        input_file = self.selected_file
        input_file = input_file.replace("\\", "\\\\")

        code = gmshtxt.insert_characters__(gmshtxt.python_code_gmsh4, input_file, 'gmsh.merge')

        filename = 'temp_code_gmsh.py'
        with open(filename, 'w') as file:
            file.write(code)

        subprocess.call([self.anotherpython, filename])

        os.remove(filename)


    def gmshbutton1_run(self, widget, function_entry):
        gmsh_points = function_entry.get_child().get_text()

        code = gmshtxt.insert_characters(gmshtxt.python_code_gmsh1, gmsh_points, 'p =')

        filename = 'temp_code_gmsh.py'
        with open(filename, 'w') as file:
            file.write(code)

        subprocess.call([self.anotherpython, filename])

        os.remove(filename)

    def gmshbutton2_run(self, widget, function_entry):
        gmsh_polar = function_entry.get_child().get_text()

        code = gmshtxt.insert_characters_(gmshtxt.python_code_gmsh2, gmsh_polar, 'string_gx =')

        filename = 'temp_code_gmsh.py'
        with open(filename, 'w') as file:
            file.write(code)

        subprocess.call([self.anotherpython, filename])

        os.remove(filename)

    def gmshbutton3_run(self, widget, function_entry):
        gmsh_globe = function_entry.get_child().get_text()

        code = gmshtxt.insert_characters_(gmshtxt.python_code_gmsh3, gmsh_globe, 'string_gx =')

        filename = 'temp_code_gmsh.py'
        with open(filename, 'w') as file:
            file.write(code)

        subprocess.call([self.anotherpython, filename])

        os.remove(filename)


if __name__ == "__main__":
    gmshwin = Gsc_gmsh()
    gmshwin.run()


