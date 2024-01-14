import gi
import numpy as np

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Gsc_calculator:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./glade_file/Gsclab0.glade")

        # 获取容器对象
        self.entry = self.builder.get_object("entry")

        # 连接按钮的信号处理函数
        self.connect_buttons()

        self.window = self.builder.get_object("Gscwindows5")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_resizable(False)



    def connect_buttons(self):
        button_ids = [
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
            "b9", "b10", "b11", "b12", "b13", "b14", "b15",
            "b16", "b17", "b18", "b19", "b20", "b21", "b22",
            "b23", "b24", "b25", "b26"
        ]


        for button_id in button_ids:
            button = self.builder.get_object(button_id)

            if button is not None:
                button.connect("clicked", self.clicked_button, self.entry)

    def run(self):
        self.window.show_all()
        Gtk.main()


    def clicked_button(self, button, entry):
        global last_operation, last_value
        # 获取按钮的标签值
        label = button.get_label()
        #获取文本框中的值
        text=entry.get_text()

        # 单独定义特殊按钮
        if label == "C":
            entry.set_text("")#清除全部
            # 用于追踪前一个操作
            last_operation = None
            # 用于保存前一个操作的值
            last_value = None

        elif label=="CE":
            entry.set_text(text[:-1])#只清除最后一个字符

            last_operation= last_operation[:-1]
            last_value =text[-1]

        elif label == "=":

            # 使用eval()计算表达式结果
            result = eval(text)
            entry.set_text(str(result))
            last_operation = ''
            last_value = str(result)

        elif label=="sin":
            try:
                value = float(last_value)
                result =np.sin(value)
                entry.set_text(last_operation+str(result))
                #last_operation = label
                last_value = str(result)
            except:
                return

        elif label=="cos":
            try:
                value = float(last_value)
                result = np.cos(value)
                entry.set_text(last_operation + str(result))
                last_value = str(result)
            except:
                return

        elif label=="tan":
            try:
                value = float(last_value)
                result = np.tan(value)
                entry.set_text(last_operation + str(result))
                last_value = str(result)
            except:
                return

        elif label=="x^(1/2)":
            try:
                value = float(last_value)
                result = np.sqrt(value)
                entry.set_text(last_operation + str(result))
                last_value = str(result)
            except:
                return

        elif label=="x^2":
            try:
                value = float(text)
                result = value**2
                entry.set_text(str(result))
                last_value = str(result)
            except:
                return

        elif label=="1/x":
            try:
                value = float(last_value)
                result = 1/value
                entry.set_text(last_operation + str(result))
                last_value = str(result)
            except:
                return

        else:
            # 添加按钮的值到文本框
            if label=="pi":

                entry.set_text(text+str(np.pi))
                last_operation = text
                last_value=str(np.pi)
            # elif label=='.':
            #     entry.set_text(text + label)
            #     last_operation=text
            #     last_value=last_value+label

            else:
                entry.set_text(text+ label)
                last_operation = text
                last_value=label


if __name__ == "__main__":
    app = Gsc_calculator()
    app.run()