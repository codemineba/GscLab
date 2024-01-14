import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numpy as np
from numpy import pi
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from sympy import symbols, sympify


class Gsc_plot:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/GscLab3.glade")

        self.comboBoxContainer = self.builder.get_object("container")
        self.comboBox = Gtk.ComboBox.new_with_entry()
        entry = self.comboBox.get_child()
        entry.set_placeholder_text("请输入或选择函数表达式")

        self.liststore = Gtk.ListStore(str)
        self.liststore.append(['x'])
        self.liststore.append(['x**2'])
        self.liststore.append(['exp(x)'])
        self.liststore.append(['log(x)'])
        self.liststore.append(['sin(x)'])
        self.liststore.append(['cos(x)'])
        self.liststore.append(['tan(x)'])

        self.comboBox.set_model(self.liststore)

        self.comboBoxContainer.pack_start(self.comboBox, True, True, 0)

        self.comboBox.set_entry_text_column(0)

        self.lower_entry = self.builder.get_object("lower")
        self.lower_entry.set_placeholder_text("请输入区间下限")

        self.upper_entry = self.builder.get_object("upper")
        self.upper_entry.set_placeholder_text("请输入区间上限")

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas_box = self.builder.get_object("canvas_box")
        self.canvas_box.pack_start(self.canvas, True, True, 0)

        self.window = self.builder.get_object("Gscwindows3")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)

        self.main_button = self.builder.get_object("main_button")
        self.main_button.grab_focus()

        self.main_button.connect(
            "clicked",
            self.plot_function,
            self.comboBox,
            self.lower_entry,
            self.upper_entry,
            self.canvas,
        )

        self.comboBox.connect('changed', self.on_function_selected)


    def on_function_selected(self, combo):
        active_iter = combo.get_active_iter()
        if active_iter is not None:
            model = combo.get_model()
            function = model[active_iter][0]
            self.set_preset_values(function)

    def set_preset_values(self, function):
        if function == 'x':
            self.lower_entry.set_text('0')
            self.upper_entry.set_text('10')
        elif function == 'x**2':
            self.lower_entry.set_text('-5')
            self.upper_entry.set_text('5')
        elif function == 'exp(x)':
            self.lower_entry.set_text('-2')
            self.upper_entry.set_text('2')
        elif function == 'sin(x)':
            self.lower_entry.set_text('-pi')
            self.upper_entry.set_text('pi')
        elif function == 'cos(x)':
            self.lower_entry.set_text('-pi')
            self.upper_entry.set_text('pi')
        elif function == 'tan(x)':
            self.lower_entry.set_text('-2*pi')
            self.upper_entry.set_text('2*pi')
        elif function == 'log(x)':
            self.lower_entry.set_text('0.01')
            self.upper_entry.set_text('10')



    def plot_function(self, button, function_entry, lower_entry, upper_entry, fig_canvas):
        function_expr = function_entry.get_child().get_text()
        try:
            x = symbols('x')
            function = sympify(function_expr)

            fig = fig_canvas.figure
            ax = fig.add_subplot(111)

            lower = eval(lower_entry.get_text())
            upper = eval(upper_entry.get_text())
            x_vals = np.linspace(lower, upper, 100)
            y_vals = np.array([function.subs(x, val) for val in x_vals])
            ax.plot(x_vals, y_vals)
            ax.set_xlabel('x')
            ax.set_ylabel('y')

            fig_canvas.draw()

            fig.delaxes(ax)
        except Exception as e:
            fig.delaxes(ax)
            print(f"Error: {str(e)}")

    def run(self):
        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    gui = Gsc_plot()
    gui.run()