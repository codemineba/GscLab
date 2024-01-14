import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


import sys
sys.path.append('./pygame_code/MineSweeping')
sys.path.append('./pygame_code/Tetris')

from pygame_code.GluttonousSnake import main as game1_py
from pygame_code.Gomoku import ManAndMachine as game2_py
from pygame_code.MineSweeping import main as game3_py
from pygame_code.Tetris import main as game4_py


def turn_game1(self):
    game1_py.main()

def turn_game2(self):
    game2_py.main()

def turn_game3(self):
    game3_py.main()

def turn_game4(self):
    game4_py.main()

class Gsc_game:
    def __init__(self):

        # 创建Gtk.Builder对象并加载Glade文件
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gscgame.glade")

        self.window = self.builder.get_object("game_window")
        self.window.connect('destroy', Gtk.main_quit)
        self.window.set_resizable(False)

        self.button1 = self.builder.get_object("button1")
        self.button2 = self.builder.get_object("button2")
        self.button3 = self.builder.get_object("button3")
        self.button4 = self.builder.get_object("button4")

        self.button1.connect('clicked', turn_game1)
        self.button2.connect('clicked', turn_game2)
        self.button3.connect('clicked', turn_game3)
        self.button4.connect('clicked', turn_game4)


    def run(self):
        # 显示窗口
        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = Gsc_game()
    app.run()