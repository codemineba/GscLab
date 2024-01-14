
# GscLab: 基于GTK界面的科学计算（scientific computing）平台

<br>


## 了解GTK：开发软件所基于的图形用户界面

<br>

 **GTK**，全称 “GIMP Toolkit”，是一个C语言开发的开源的跨平台的GUI（Graphical User Interface）工具包，**GUI** 是应用程序提供给用户操作的图形界面，包括窗口，菜单，按钮等图形界面元素，我们经常使用的QQ软件，360安全卫士等均为GUI程序。最初的GTK是为图像处理软件 GIMP（GNU Image Manipulation Program）开发的。如今，GTK已经发展成为一个独立的项目，广泛应用于众多桌面应用程序、工具、小部件和游戏等的开发中。

类似的，像这样用于开发图形界面的GUI开发工具还有
1. *Swing*：完全由Java开发的轻量级（跨平台）组件，是JDK的第二代GUI框架
2.  *Qt*：核心由C++开发的跨平台应用程序开发框架，提供了一套丰富的工具和库，用于开发图形用户界面（GUI） 应用程序、嵌入式应用程序以及跨平台移动应用程序。
3. *.NET Windows Forms*：基于 C# 开发的 Windows 桌面应用程序开发框架 ，属于.NET 平台的一部分
4. *Electron*：一个基于Web技术的开源框架，用于构建跨平台的桌面应用程序，使用HTML、CSS和JavaScript开发。
5. *JavaFX* ： Java 平台的一部分，它提供了丰富的图形界面控件和效果，并支持多媒体和动画功能。JavaFX 可以用于开发跨平台的桌面应用程序和富互联网应用。它具有良好的可扩展性和灵活性，开发者可以利用 JavaFX 提供的强大 API 创建各种设备上的用户界面。
......

### ***GTK的特点包括：***
###### 面向对象式的API:
Glib 是 GTK 的基础，提供了面向对象系统的支持。GObject 是 Glib 中的面向对象机制，提供了一种用于创建、管理和操作对象的框架，同时也作为GLib 中的核心库，用于支持对象的封装、继承、多态以及信号和插件系统等特性。作为一个面向对象编程的库，GObject 旨在提供一种灵活、轻量级的对象系统，方便开发人员构建和管理对象，它是 GNOME 桌面环境中的基础模块之一，被广泛用于开发 GNOME 应用程序。同时，GObject 也可用于将 GTK+ 绑定到多种开发语言，包括 C++、Python、Perl、Java、C#、PHP 等高级语言。
######  跨平台：
GTK是跨平台的工具包，可以在多个操作系统上运行，如Linux、Windows、macOS等。这使得开发人员能够编写一次代码，在不同的平台上部署和运行GTK应用程序，从而实现更广泛的应用程序使用和可拓展性。

###### 可扩展性：
1. 插件机制：GTK提供了插件机制，允许开发人员通过插件来增加或修改GTK的功能和行为。开发人员可以编写自定义插件并将其集成到GTK应用程序中，以满足特定需求或增加新的功能。

2. 自定义主题：GTK通过使用CSS（层叠样式表）来定义和修改应用程序的外观和样式。开发人员可以轻松地创建自定义主题，并将其应用于GTK应用程序，以实现独特的界面风格。
3. 可视化界面设计：GTK提供一个直观的用户界面设计工具——Glade，使开发人员能够通过拖放和配置控件来创建用户界面。这种可视化的设计方式使得界面设计更加直观和高效。并且实现代码分离，通过使用 Glade，开发人员可以将界面的布局和属性配置保存在独立的 XML 文件中，然后在应用程序中加载并动态构建界面。这种分离能够提高代码的可维护性和重用性。



总之，
GTK已经被广泛应用于许多知名的应用程序，如GNOME桌面环境、GIMP、Inkscape等。它提供了丰富的功能和灵活性，使开发人员能够轻松地创建出功能齐全、易于使用的应用程序。


<br>

## 了解科学计算：科学活动的三大方法之一 “实验，理论，科学计算”

<br>

<br>

## 开发前的准备工作：配置环境
GTK的界面设计可以采用多种语言编写，最常用的包括C，C++，Python... 这里我们采用Python，可以简单而快速地创建界面，并且具有大量的第三方库和工具，能使得开发更加高效
使用GTK之前，我们得先配置GObject包，里面提供了很多工具包括GTK, GStreamer, WebKitGTK, GLib, GIO等等。
想在windows上直接安装PyGobject总是安装不了，无论在编辑器中用工具还是用pip都行不通，原因是缺少部分依赖，想要安装PyGobject必须在模拟Linux的环境中才能安装，所以首先要下载Msys2，这是一个基于cygwin的软件发行版，为windows提供了一套类似于Linux的开发环境。这是安装地址 [https://www.msys2.org/](https://www.msys2.org/) 安装完Msys2并配置好gcc后，便可进入[https://pygobject.readthedocs.io/en/latest/getting_started.html](https://pygobject.readthedocs.io/en/latest/getting_started.html) 中找到windows的配置方法，按照步骤配置好gtk3，python3，Gobject的交互式环境（网址上配置的是gtk4，但由于gtk4目前还无法于matplotlib兼容，所以我们配置gtk3，只需把gtk4改成gtk3即可）
配置完成后，在Msys2的文件夹下找到mingw64，在里面的bin目录中有刚才配置好gtk3的python解释器（python3.exe）可直接使用或将其放到专业的编辑器下使用即可（刚放到编辑器下时可能会显示一些报错但并不影响运行，根据提示更新相关库可减少报错）
由于配置得到的是一个新的python解释，很多常用的第三方的工具包都没有配置，需要手动下载，用编辑器里的工具下载同样有问题，我们可以采用pip或者pacman(Mysy2中提供的包管理器)，注意要在Msys2的Mingw64 shell环境中下载（那个环境下的python默认是刚刚配置好的python），不能直接在windows的终端下载。

<br>

<br>

#  《开发日志》

<br>


既然要开发一款软件，首当起冲需要解决的问题就是界面的ui设计，包括部件的设置和界面的布局等，以及交互式设计，包括用户的输入，引导，部件之间的信号，对用户的反馈等。
## 界面的UI与交互式设计
Gtk拥有丰富的界面开发工具包，利用Gtk可以更加便捷地选择合适插件并将其配置到主界面上，其中实现该界面设计的方法大致有两种，分别是代码实现和Glade设计。

## 代码实现
界面开发过程中，我们首先要提供一个载体窗口，且可自定义名称和大小等。

```python
window = Gtk.Window()#创建一个界面窗口
window.set_title("My Window")#设置窗口名称
window.set_default_size(200, 100)#设置窗口的默认大小
```
在此基础上，由于Gtk提供了许多小部件，如按钮、标签、文本框、下拉列表等，可以根据需求选择合适的插件用于构建交互式界面。

```python
# 创建布局容器(可调节位置)
box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)#创建一个容器
window.add(box)#将容器添加到窗口中

# 创建标签
label = Gtk.Label()
label.set_text("Hello, World!")#设置标签内容
box.pack_start(label, True, True, 0)#将标签添加到容器

# 创建按钮
button = Gtk.Button.new_with_label("Click Me")#创建按钮并可设置按钮名称
box.pack_start(button, True, True, 0)#将按钮添加到容器中
```
自定义完成后，可添加Gtk.main_quit()函数在关闭窗口时结束进程，并使用show_all()函数用以显示界面，利用Gtk.main()启动Gtk主循环。

```python
# 关闭窗口时退出GTK主循环
window.connect("destroy", Gtk.main_quit)#连接函数，退出时结束进程

# 显示窗口及其内容
window.show_all()
# 启动GTK主循环
Gtk.main()
```
这样，就实现了一个简单页面的设计。
![在这里插入图片描述](https://img-blog.csdnimg.cn/475fb15e4216487b840769de6823db9d.png#pic_center)

然而，由于代码操作的局限性，存在界面设计单一，不同插件可能存在冲突，导致操作不便。为解决这一问题和进一步优化界面排版，考虑使用Glade。

## Glade设计
Glade是一个可视化用户界面设计器工具，它允许开发人员通过图形化的方式创建并设计Gtk界面，同时允许设置属性和信号，定义界面的层次结构，而无需手动编写界面定义文件。可以说，Glade 提供了一个直观的界面来快速构建和定制 GTK 应用程序的用户界面。
Glade文件是由工具生成XML文件，其中包含了界面的层次结构，对象属性，信号连接等信息，描述了用来构建Gtk用户界面的各个部分。
由于Glade 文件本身并不包含应用程序代码逻辑，而是专注于描述界面的外观和结构。因此通过将 Glade 生成的 .glade 文件与应用程序的代码连接起来，并通过信号和回调函数进行用户交互。


Glade界面主要包含三部分，分别是保存和导出，设计界面，属性编辑器。
![在这里插入图片描述](https://img-blog.csdnimg.cn/8cf1bbb22f784af7922957fc164464ed.png#pic_center)
### 界面设计
在设计界面里，首先需要创建适当的顶层窗口用于形成界面，其次通过选择容器、控制、显示等组件对界面进行设计和排版。Glade提供丰富的部件供使用者选择，为方便布局，建议在顶层窗口创建完成后添加容器中的GtkFixed以提高添加部件的自由度。
![在这里插入图片描述](https://img-blog.csdnimg.cn/1da9b29c53094cb5b2712a668d94e8f0.png#pic_center)
此外，容器的种类丰富，其中的GtkBox可根据需求确定行数和列数，在界面设计中使用较广泛。
![在这里插入图片描述](https://img-blog.csdnimg.cn/a8fd9b0d7c564c8e8febeb4669d39c8d.png#pic_center)
控制类部件和标签类部件选择较多，供用户在实现不同功能时根据具体需求进行界面设计，例如：
按钮（GtkButton）
![Gtk.Button](https://img-blog.csdnimg.cn/43aef151a1af47dca4dbcec8133a0995.png#pic_center)
可编辑部件（GtkEntry）
![在这里插入图片描述](https://img-blog.csdnimg.cn/e09e63c88a5549cca9cc089f57bfa7c5.png#pic_center)
可调节按钮（GtkSpinButton）
![在这里插入图片描述](https://img-blog.csdnimg.cn/1caa595338f349a4888bf20008ffd727.png#pic_center)
可下拉列表框（GtkComboBox）
![在这里插入图片描述](https://img-blog.csdnimg.cn/429d0be33f1c49aab86e6bbec5fbc5a2.png#pic_center)
标签（GtkLabel）
![在这里插入图片描述](https://img-blog.csdnimg.cn/b76f906cb1a945498464ec4788d13267.png#pic_center)
诸如此类的可调节部件，不仅为使用者设计界面提供了方便，还一定程度上提高了界面排版的美观度。

当然，也存在一些部件的功能无法仅依靠Glade设计达到用户需求，那么我们需要将其与代码结合，根据不同难题选择相对应的方法进行解决。
#### .glade文件与代码结合
为了更好的实现交互，考虑将glade文件与代码结合。为实现这一目的，只需要在Glade中设置好顶层容器的ID名，在代码实现中进行交互即可。
![在这里插入图片描述](https://img-blog.csdnimg.cn/4f00f81e7d224fe680beeb0520917b17.png#pic_center)


```python
#创建对象
builder = Gtk.Builder()
#将Glade文件中的布局和部件加载到Builder对象中
builder.add_from_file("GscLab.glade")
.
.
.
#连接窗口
window = builder.get_object("Gscwindows")
```
其中在Glade中设置容器后，选择在代码中对该容器进行操作，也是只需要定义好该容器名。

#### 特殊按钮
在设置GtkComboBox插件时，如果单单想要可下拉控制窗格，在Glade中选择插入并设置即可。但如果想要一个可编辑的下拉控制窗口，可先在Glade界面中布局好一个可供添加控制选项的容器，然后选择使用GtkComboBox.new_with_entry()函数进行操作，在此基础上可以添加下拉窗口选项。
```python
# 获取容器对象
#获取已有容器ID
comboBoxContainer = builder.get_object("container")
#创建可编辑的下拉表
comboBox = Gtk.ComboBox.new_with_entry()
# 创建列表存储对象
liststore1 = Gtk.ListStore(str)
liststore1.append(['sinx'])
# 将列表存储对象设置为 Gtk.ComboBox 模型
comboBox.set_model(liststore)
# 将 Gtk.ComboBox 添加到容器中
comboBoxContainer.pack_start(comboBox, True, True, 0)
comboBox.set_entry_text_column(0)
```
这样便得到一个可编辑的下拉列表框。
![在这里插入图片描述](https://img-blog.csdnimg.cn/8ab6444d0ca842a0b13230df79c889cb.png#pic_center)
### 属性编辑
在设置好部件的基础上，属性编辑器主要对各组件进行属性设置，如大小，ID，位置，样式特性等，其中信号关联着对应应用程序函数的代码，用以实现具体的功能。
而实现部件间信号的交互，我们提供两种方法。
#### 方法1
通过更改属性栏中信号的名称，在代码中以对应名称为函数名编写功能。
例如，我们定义一个按钮，将其信号中的clicked行更名为click。
![在这里插入图片描述](https://img-blog.csdnimg.cn/6012ba8777c04fd5aedc2fe177f69e19.png#pic_center)
再在代码实现中定义同名函数即可实现相应功能。

```python
#定义同名函数
def click(self):
	print("Hello,world")
```

#### 方法2
不使用属性栏中的信号，仅在代码中定义函数后，利用connect函数与相应部件进行连接。

```python
button1=builder.get_object("button1")#获取已知的按钮id
button1.connect("clicked", "目标函数名")#连接函数
```
这样，就不需要额外在Glade中更改函数名就实现了函数连接。
相比方法1，方法2更易于修改和维护，简化流程的同时提高了程序的可扩展性和可读性。
因此，在GscLab中，我们选择采用方法2对功能进行开发。

<br>
可以看出，Glade 的使用优势在于它的用户友好性、可视化设计和快速迭代开发，它可以帮助你以更高效和易于维护的方式创建复杂的用户界面。而Glade与代码结合使用，一方面解决一些功能在Glade里的不可设性，另一方面也提高了应用的可拓展性和开发效率。



<br>

# 核心功能开发（第一版）

在解决完ui与交互的问题后，便来到了开发的关键——核心功能开发。
**核心功能**：

1. 计算器
2. 绘制函数图像
3. gmsh网格显示
4. 数值分析的误差可视化

<br>


### 1.  计算器
#### 确定需求

 1. 用户可以通过按键进行运算
 2. 用户可以选择函数参与计算

#### 技术难点

 1. 触发按键后将值传递给文本框
 2. 实现输入目标计算式后进行有顺序的四则运算

#### 解决思路
1. 通过构造函数clicked_button()，获取按钮标签值 get_label 后，利用entry.set_text()即可获取选择值。

```python
 last_operation = None # 用于追踪前一个操作
 last_value = None # 用于保存前一个操作的值
 
 def clicked_button(self, button):#定义函数
     global last_operation, last_value 
     label = button.get_label()#获取按钮的标签值
     text=entry.get_text()#获取文本框中的值
     # 单独定义特殊按钮
     if label == "C":
        entry.set_text("")#清除全部，即文本框获取到""(空)
        last_operation = None# 用于追踪前一个操作
        last_value = None# 用于保存前一个操作的值

     elif label=="CE":
         entry.set_text(text[:-1])#只清除最后一个字符，除最后一个字符对其余进行切片
         last_operation= last_operation[:-1]#更新前一个操作
         last_value =text[-1]#更新前一个值

     else:
         # 添加按钮的值到文本框
          if label=="pi":
             entry.set_text(text+str(np.pi))#将之前文本框内内容和新内容重新传入文本框
             last_operation = text#更新前一个操作
             last_value=str(np.pi)#更新前一个值

          else:
              entry.set_text(text+ label)#若按键标签为其他数字，则将原文本框内容和该数字重新传入文本框
              last_operation = text#更新前一个操作
              last_value=label#更新前一个值
```
2. 解决有优先级的运算，需要使用Python的原生函数eval()函数，它用于对字符串中的表达式进行求值，即将字符串当转化为有效的表达式来求值，并返回计算结果。尽管存在一定的风险，但在实现计算器程序上我们认为是可以使用的。

```python
elif label == "=":
	#text为获取文本框内的计算式
	result = eval(text)# 将text传入eval()，计算表达式结果
	self.entry.set_text(str(result))#将结果出入到文本框
```


<br>

界面图片如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/76fd58bae0ae45168a9733f0ed7cfa4c.png#pic_center)
#### 目前存在不足：
1. 函数功能的实现有待完善
2. 清除操作中，如果仅选择清除最后一个字符，则无法正确使用函数，除非完全清除

#### 未来改进方向：
1. 在现有基础上增加函数功能，便于更多常用函数的实现
2. 使函数的利用更加具有普适性
3. 解决代码冗余，提高实现效率
<br>
<br>

### 2. 绘制函数图像
#### 确定需求
 1. 用户可以输入或选择示例函数
 2. 用户可以手动输入函数上下界
 3. 用户选择实例函数后会出现每一个函数相应的上下界
#### 技术难点：
1. 将图绘制在GTK的窗口上
2. 从文本框获取到函数的字符串后转化为实际的数学函数
3. 选择不同函数时对应要出现不同的上下界
#### 解决思路：
1. 想要绘制函数图像，就得有画图的工具，在Python中提到画图首先想到的工具便是matplotlib包。值得一提的是，Python的matplotlib包对GTK非常友好，专门提供了一个模块叫做backend_gtk3agg，这是一个GTK agg的后端模块（agg 是 Matplotlib 库中的一个绘图渲染引擎），采用这个模块里的FigureCanvasGTK3Agg类可以很方便的将Matplotlib 的图形渲染到 GTK3 窗口上，具体细节如下：

```python
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

# 创建一个绘图画布类
fig = Figure()

# 创建了一个基于 GTK3 Agg 后端的 FigureCanvasGTK3Agg 对象，
# 并将其与 fig 画布对象进行关联便能在上面绘制图形
canvas = FigureCanvas(fig)

# 将canvas放置在GTK的容器便能实现在GTK窗口绘制
canvas_box.pack_start(canvas, True, True, 0)

# 可以再次获取 FigureCanvas对象关联的 Figure对象
fig = canvas.figure

# 在 fig 上创建一个子图，参数 (111) 指定子图的位置和尺寸，
# 其中的三个数字分别代表子图的行数、列数和位置，这里的 (111) 表示一个只有一个子图的 1x1 网格，而且位置在第一个（唯一）的子图上。
ax = fig.add_subplot(111)

# x_vals：绘制图形的x坐标的数组
# y_vals：绘制图形的y坐标的数组
ax.plot(x_vals, y_vals)

```

2. 将一个函数的字符串像"x**2", "sin(x)",转化为python中可以接收参数的数学函数，自己写算法会比较麻烦，需要考虑的情况太多，代码冗长，所以引入一个新的python包 **sympy**，
SymPy是一个用于符号计算的Python库，它旨在为数学领域的计算提供强大的功能。SymPy可以进行符号计算、代数运算、求解方程、微积分、线性代数、离散数学等多种数学操作。
采用 sympy 的 sympify函数，便可直接将字符串函数转化为数学函数，具体细节如下：

```python
# 导入需要的模块和函数
from sympy import symbols, sympify
import numpy as np

# 创建符号变量x
x = symbols('x')

# function_string：待转化的一个函数字符串
# 将字符串表示的函数转化为SymPy表达式
function = sympify(function_string)

# lower：下界
# upper：上界
# 在指定范围内生成100个等间距的x值
x_vals = np.linspace(lower, upper, 100)

# 遍历每个x值，计算对应的y值并存储在数组中
y_vals = np.array([function.subs(x, val) for val in x_vals])

# 得到 x_vals 和 y_vals 后便可通过ax.plot(x_vals, y_vals)绘制函数

```


3. 想要实现实现可编辑可选择函数的下拉文件框，插入部件ComboBox并设置相关属性即可，但要实现选择完函数后对应的出现一些特征的上下界需要连接其他的信号，在这里需要用到一个不太常见的用户信号 " changed "将其连接到ComboBox中，便可检测下拉列表的选项是否发生变动，连接函数后即可做出相应变动后的操作。具体细节如下：

```python
# 检测下拉列表选项是否发生变化，每次变化后调用on_function_selected函数
comboBox.connect('changed', on_function_selected)


def on_function_selected(self, combo):

    # 获取ComboBox的当前选择的迭代器对象（迭代器是用来访问容器元素的一种方式，它可以遍历容器中的元素并返回当前的元素。）
    active_iter = combo.get_active_iter()
    # 如果选择不为空，继续执行下面代码
    if active_iter is not None:
        # 获取模型对象
        model = combo.get_model()
        # 从模型中获取当前函数值
        function = model[active_iter][0]
        # 以函数值为参数执行set_preset_values函数，对不同的函数提供不同的操作
        self.set_preset_values(function)

# 不同的函数有相应的上下界的实例取值
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
            
```





<br>

界面图片如下：


![在这里插入图片描述](https://img-blog.csdnimg.cn/807d8b59bb094ae58af6a8b9e2cfc69c.png#pic_center)



#### 目前存在不足：
1. 函数形式单一，图象单一
2. 函数区间只能手动输出，灵活度低

#### 未来改进方向
1. 可以输入带参数的函数（添加相应参数的框，可灵活的改变参数的大小）
2. 可以自定义函数曲线的颜色，粗细等特征

<br>
<br>

### 3. gmsh网格显示

#### 确定需求：
 用户可以通过提供网格文件（.msh .off .geo）或者输入/选择二维顶点坐标，极坐标，球坐标生成对应形状的网格。
#### 技术难点：
1. 由于在Msys2这个开发环境中，使用MinGW的Pacman能下载的包有限（找不到gmsh，下载不了），使用pip也存在一定问题（使用pip install <包名> 最后会出现 pip subprocess to install build dependencies did not run successfully. This error originates from a subprocess, and is likely not a problem with pip 的提示），如果直接暴力把其他解释器配置好的包迁移过来又存在依赖问题...（总之MinGW的python解释器不能配置gmsh包）

2. （已经写好了提供顶点或函数生成网格的API工具包） 在已有的API中，有一行代码是用np.linspace 通过提供上下界得到坐标的列表，而用这个函数得到的数据类型是np.array，但sympy的函数（字符串通过sympify转化的函数）不能接受np.array的数据类型。
#### 解决思路
1. 针对技术难点1，以下提供三种思路：
##### 思路1：
 直接调用gmsh的执行文件，打开其内置窗口，给定msh，off，geo文件，生成网格。

采用**subprocess**包，这个包是 Python 标准库中的一个模块，用于在程序中创建和管理子进程，以及与子进程进行交互。具有很强大且灵活的功能，在这里主要使用它的**call**函数，这个函数用于执行外部命令并等待其完成。

```python
import subprocess

# 设置gmsh执行文件的路径和输入文件的路径
gmsh_path = "C:\msys64_GTK3\mingw64\lib\python3.11\Scripts\gmsh.bat"
input_file = "./data/test.msh"

# 调用gmsh执行文件生成网格
subprocess.call([gmsh_path, input_file])
```
这里的gmsh.bat文件是普通的python3.11解释器下载gmsh包后在python311目录下的Scripts文件夹中生成的（只用下载了gmsh的python包才能出现），拷贝到其他路径下并使用其打开网格文件。（直接使用从官网上下载的gmsh.exe也行）

***优点***：操作简单，需求单一，容易实现嵌入
***缺点***：功能单一，只能提供给网格文件才能生成网格，不能通过给定点和方程来生成。

##### 思路2：
嵌套解释器：既然Msys2中的解释器不能配置gmsh包，那就在py文本中手动调用另一个python解释器。

```python
import subprocess

# 替换为你想要使用的解释器的完整路径
python_interpreter = r'C:\Users\27966\AppData\Local\Programs\Python\Python311\python.exe'

# 调用特定的解释器并执行脚本
subprocess.call([python_interpreter, r'D:\procedure\python\gmsh_made\model_basic1.py'])
```
当然，也可以在这个脚本下直接写入嵌套的脚本，放到一个临时的脚本，最后在把临时脚本删除即可，这样更方便且容易实现与GTK的嵌入

```python
import subprocess
import os

# 定义要运行的 Python 代码
python_code = '''
import gmsh

gmsh.initialize()  # 初始化
gmsh.model.add("model1")  # 创建模型

lc = 1e-1  # 设置网格尺寸值

# 创建点
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
# 创建线
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 2, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
# 创建边
gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
# 创建面
gmsh.model.geo.addPlaneSurface([1])

gmsh.model.geo.synchronize()  # 同步到模型
gmsh.model.mesh.generate(2)  # 生成网格
gmsh.write("triangleMesh.off")  # 生成.msh文件
gmsh.fltk.run()  # 图形界面显示
gmsh.finalize()  # 关闭gmsh
'''

# 将代码保存到临时文件中
filename = 'temp_code.py'
with open(filename, 'w') as file:
    file.write(python_code)

# 使用另一个解释器执行临时文件
python_interpreter =  r'C:\Users\27966\AppData\Local\Programs\Python\Python311\python.exe'  # 替换为另一个解释器的路径
subprocess.call([python_interpreter, filename])

# 删除临时文件
os.remove(filename)
```
***优点***：操作性极强，可以充分解决不能使用gmsh包的问题，实现几乎gmsh能做的所有工作
***缺点***：需求大，需要单独再配置一个python解释器，以及带来的命名空间冲突、资源管理以及性能支持方面的问题。
##### 思路3：
不使用gmsh的图形窗口，与matplotlib一样将图像画在自主开发的GTK窗口中。（同样也是使用matplotlib画图）

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

# 读取 off 文件
file_path = "./data/edgetext.off"

with open(file_path, "r") as file:
    lines = file.readlines()

# 读取顶点坐标和面的连接信息
num_vertices, num_faces, _ = map(int, lines[1].split())

vertices = []
faces = []
for line in lines[2:2+num_vertices]:
    vertex = list(map(float, line.split()))
    vertices.append(vertex)

for line in lines[2+num_vertices:2+num_vertices+num_faces]:
    face = list(map(int, line.split()[1:]))  # 忽略第一个值，因为它表示顶点数量
    faces.append(face)

# 创建 GTK 窗口
window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(400, 300)

# 创建 Matplotlib 的 Figure 和 Axis
figure = plt.figure()
axis = figure.add_subplot(111, projection="3d")

# 绘制网格
for face in faces:
    x = [vertices[i][0] for i in face]
    y = [vertices[i][1] for i in face]
    z = [vertices[i][2] for i in face]
    axis.plot(x + [x[0]], y + [y[0]], z + [z[0]], 'r-')

# 设置坐标轴范围
min_coord = min(min(vertices, key=lambda v: v[0])[0],
                min(vertices, key=lambda v: v[1])[1],
                min(vertices, key=lambda v: v[2])[2])
max_coord = max(max(vertices, key=lambda v: v[0])[0],
                max(vertices, key=lambda v: v[1])[1],
                max(vertices, key=lambda v: v[2])[2])
axis.set_xlim(min_coord, max_coord)
axis.set_ylim(min_coord, max_coord)
axis.set_zlim(min_coord, max_coord)

# 将 Matplotlib 的 Figure 对象转换为 GTK 的图像部件
canvas = FigureCanvas(figure)
window.add(canvas)

# 显示 GTK 窗口
window.show_all()

# 启动 GTK 的事件循环
Gtk.main()
```
<p align="center">
  <img src="https://img-blog.csdnimg.cn/f7de704c25f04a4bb3860f8b0461b261.jpeg" alt="图片描述" width="500" height="300">
</p>

***优点***：将网格图像画到自主开发的图像界面上，拓展性提高
***缺点***：与思路1一样，需要提供网格文件才能生成，从效率上看，当网格文件较为复杂时，算法执行时间较长，再从图像呈现上看，智能，渲染，效果，优化明显不如gmsh，特别当网格较为复杂时，Gtk窗口可能无法达到所需的性能水平。

<br>

由于采取嵌套解释器的方法才能方便用到之前写好的gmsh的工具包，才能方便实现需求，所以采取**思路2**, 即将选中的函数，顶点插入到已经写好的gmsh工具包的API中的合适位置，因为第一步只需插入字符串，所以合适位置的确定由字符串的查找函数 find，参数设置为对应的函数前的特殊字符串像"p =", "string_gx =", "gmsh.merge" (能够打开网格文件的函数) 即可。具体细节如下：

```python
python_code_gmsh1 = '''
import gmsh
import gmsh_tools as tools
import numpy

# 根据二维顶点坐标[x, y]生成对应网格图像的API

gmsh.initialize()

# 顶点坐标（二维，形如（x, y））(列表坐标的顺序需要符合首尾相连的顺序)
p = 

# 由给定的顶点坐标生成网格 (p为二维坐标列表)
model1 = tools.model_made_point(p)

gmsh.model.occ.synchronize()  # 同步
gmsh.model.mesh.generate(2)  # 生成网格

gmsh.fltk.run()  # 图形界面显示
gmsh.finalize()  # 关闭gmsh

'''

def insert_characters(original_str, insert_str, position):
    index = original_str.find(position)
    if index == -1:
        return "原始字符串中找不到 " + insert_str

    position = index + len(position) + 1  # 'p=' 的后面位置

    return original_str[:position] + insert_str + original_str[position:]
```

<br>

2. 由于sympy函数不能接收np.array的数据类型，所以必须要对二者之一做出转化，同样提供两种思路，要么将sympy函数转为numpy函数，要么让sympy的函数单独接收数组里的每一个值。

 ##### 思路1:

将sympy函数转numpy函数可以用sympy的 lambdify 函数，可以写个函数借口直接把字符串转为numpy函数，具体细节如下：

```python
from sympy import sympify, Symbol
from sympy.utilities.lambdify import lambdify

def string_to_function(expression):
    x = Symbol('x')  # 创建符号变量x
    f = sympify(expression)  # 将字符串表达式解析为SymPy表达式
    f_lambda = lambdify(x, f, 'numpy')  # 将SymPy表达式转换为NumPy函数
    return f_lambda
```

当然，这个只能是函数表达式中只有一个未知数x的情况下才能用，要是函数表达式中有两个未知数x，y，则需设置两个符号变量，扩展代码如下：

```python
def string_to_function(expression):
    if "y" not in expression:
        x = Symbol('x')
        f = sympify(expression)
        f_lambda = lambdify(x, f, 'numpy')
        return f_lambda
    else:
        x = Symbol('x')
        y = Symbol('y')
        f = sympify(expression)
        f_lambda = lambdify((x, y), f, 'numpy')
        return f_lambda
```

#### 思路2：
可以让np.array中的每一个元素单独输入sympy函数中计算，用到subs函数（功能1便采用这种方法），具体细节如下：

```python
import numpy as np
import sympy

"""这是工具包中给定极坐标生成网格的API的部分代码"""

# g: 极坐标方程的函数 (在这种情况下g是sympy的函数)
# a, b: theta的左右边界(默认为[0, 2*pi])
# num: 均匀间隔点的个数
def model_made_polar(g, num, a=0, b=2 * np.pi):
    # 计算定义域范围内的x坐标和y坐标的值（得到np.array的数据类型）
    theta = np.linspace(a, b, num)
    
    # 修改前(思路一的写法): p = g(theta)
    # 修改后，让g单独计算theta中的每一值
    x = x = Symbol('x')
    p = [g.subs(x, theta_) for theta_ in theta]
    
    x = np.cos(theta) * p
    y = np.sin(theta) * p
    
    """... 创建点，创建边 ...
       ...
    """
```
很显然，思路二的写法不太符合python习惯，加之转为numpy的函数具有更大的操作空间，所以采取**思路1**

<br>
界面图片如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/75ff076981f24b7d9e275e8b9979b1dc.png#pic_center)
#### 目前存在不足：
1. 当gmsh窗口打开后，点击上面GTK的窗口会出现进程崩溃的情况
2. 只能用二维坐标，极坐标和球坐标生成网格
3. 不能更改网格粗细和曲线上的间隔点的个数

#### 未来改进方向：
1. 争取解决进程崩溃的情况
2. 增加三维坐标，参数方程的方法生成网格
3. 增加网格尺寸值和曲线间隔点的可更改设置
4. 增加可以选择是否生成生成off文件或msh文件的选项
5. 对于三维网格，增加选择生成面网格或体网格的选项 

<br>
<br>

### 4. 数值分析的误差可视化

#### 	确定需求：
1. 用户可以输出/选择核心算法，插值点，原函数，边界条件
2. 将原函数和拟合函数绘制在一个窗口上，方便对比拟合效果
3. 设置switch可以切换是否显示原函数/拟合函数的图像

#### 技术难点：
1. 设置两个switch是否显示原函数和拟合函数

#### 解决思路
1. 在采用ax.plot绘制完图线后，需要通过python的解包操作提取ax.plot返回的包含折线的列表的第一个元素（折线对象），这个折线对象有一个方法叫做set_visible，顾名思义，可以对其进行传值True或False来控制这个折线对象是否可视。再通过连接 switch 的标志性信号 "notify::active"，来设置是否能显示折线的函数。具体细节如下：

```python
# 通过解包操作获取绘制的折线对象
line1, = ax.plot(new_x_list, new_y_list, color='red', linestyle='-', label='拟合函数')
line2, = ax.plot(new_x_list2, new_y_list2, color='black', linestyle='--', label='实际函数')

# 定义调节switch后的信号函数 （switch的函数需要设置两个参数，但第二个参数无实际意义）
def on_switch_activated2(switch, gparam):
    # switch的状态如果处于 "ON"
    if switch.get_active():
        # 折线可视
        line2.set_visible(True)
    # switch的状态如果处于 "OFF"
    else:
        # 折线不可视
        line2.set_visible(False)
    # 每次调节switch后都要关系状态
    win_plt_inter.canvas.draw()

def on_switch_activated1(switch, gparam):
    if switch.get_active():
        line1.set_visible(True)
    else:
        line1.set_visible(False)
    win_plt_inter.canvas.draw()

# 连接函数和"notify::active"信号到switch
win_plt_inter.button1.connect("notify::active", on_switch_activated2)
win_plt_inter.button2.connect("notify::active", on_switch_activated1)
```
<br>
 	
 
 界面图片如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c8011ce4b7a843418ea3008bd9d62685.png#pic_center)


<br>

![在这里插入图片描述](https://img-blog.csdnimg.cn/0279a638617244dc8c4b4962d13fb702.png#pic_center)

#### 目前存在不足：
1. 代码的逻辑部分不合理（按下“绘制”按钮后才创建绘图窗口和开始绘制图象）
2. 只能绘制有原函数的图象，函数值和导数值的文本框实际没用
3. 只能再给定的插值节点的最大最小值为上下界的区域内绘制拟合函数图像，在插值节点之外的区域不能看到拟合效果

#### 未来改进方向：
1. 更改代码逻辑，创建绘图窗口和绘制图像在按下“绘制”按钮之前完成，将canvas（FigureCanvasGTK3Agg 对象）作为参数传入"绘制"按钮的连接函数中
2. 增加不提供原函数也能看拟合函数的功能
3. 将插值节点和绘制图像的区间分开输入（选择提供的插值节点区间后默认以插值节点的最大最小值为绘制区间的上下界）
4. 持续更新功能，函数逼近，数值积分，微分 ...



 


