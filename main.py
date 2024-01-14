import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

import function as func
import aboutDialog as about
import helpfile as help

import gmsh

def jump_function(self):
    function_win = func.Gsc_func()
    function_win.run()

def jump_help(self):
    help_win = help.Gschelp()
    help_win.run()


builder = Gtk.Builder()
builder.add_from_file("./glade_file/Gsclab1.glade")

window = builder.get_object("Gscwindow1")
window.connect("destroy", Gtk.main_quit)
# 窗口不可调整大小
window.set_resizable(False)

button_about = builder.get_object("aboutbutton")
button_help = builder.get_object("helpbutton")
button_begin = builder.get_object("Gscbutton_begin")
button_close = builder.get_object("closebutton")


button_about.connect("clicked", about.show_about_dialog)
button_begin.connect("clicked", jump_function)
button_help.connect("clicked", jump_help)
button_close.connect("clicked", Gtk.main_quit)


window.show_all()

Gtk.main()

