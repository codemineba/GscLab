import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


with open('./tools_file/license.txt', 'r')as file:
    license_str = file.read()

def load_and_scale_image(file_path, width, height):

    original_pixbuf = GdkPixbuf.Pixbuf.new_from_file(file_path)


    scaled_pixbuf = original_pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)

    return scaled_pixbuf


def on_about_dialog_response(dialog, response_id):
    if response_id == Gtk.ResponseType.CLOSE or response_id == Gtk.ResponseType.DELETE_EVENT:
        dialog.destroy()

def show_about_dialog(widget):
    builder = Gtk.Builder()
    builder.add_from_file("./glade_file/GscAboutDialog.glade")
    about_dialog = builder.get_object("GscaboutDialog")
    about_dialog.set_title("About Scientific computing")
    about_dialog.set_program_name("GscLab")
    about_dialog.set_version("1.1.0")
    about_dialog.set_comments("Scientific computing, Omnipotent\n\n科学计算, 无所不能")
    about_dialog.set_authors(["张艾平 孙悦 蔡明宇 刘芷希"])
    about_dialog.set_license_type(Gtk.License.CUSTOM)
    about_dialog.set_license(license_str)

    size = 1.2
    # 加载并缩放图片
    logo_pixbuf = load_and_scale_image("./picture/GscLogo2.png", 87 * size, 58 * size)
    about_dialog.set_logo(logo_pixbuf)

    # 设置对话框的宽度和高度
    about_dialog.set_default_size(440, 300)

    about_dialog.connect("response",  on_about_dialog_response)

    about_dialog.run()



