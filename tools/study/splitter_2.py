# 本节主要学习了设置分裂器尺寸
# 以及分裂器的 连接信号
# splitter.splitterMoved.connect(lambda: show_hide_widget(splitter))



from PyQt5.QtWidgets import QApplication, QSplitter, QWidget, QVBoxLayout, QPushButton

# 创建应用程序实例
app = QApplication([])

# 创建两个简单的控件，例如两个 QPushButton
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")



# 创建 QSplitter 实例
splitter = QSplitter()

# 添加控件到 QSplitter
splitter.addWidget(button1)
splitter.addWidget(button2)

# 设置两个控件的比例，例如 1:3
# 注意：这里的数字代表的是比例，而不是绝对大小
splitter.setSizes([100, 300])

# 设置比例
# splitter.setStretchFactor(1, 1)
# splitter.setStretchFactor(0, 3)
# splitter.setSizes({1000,2000});

# 连接信号
splitter.splitterMoved.connect(lambda: show_hide_widget(splitter))


# 创建一个简单的窗口布局并添加 splitter
window = QWidget()
layout = QVBoxLayout(window)
layout.addWidget(splitter)
window.setLayout(layout)

# 显示窗口
window.show()
def show_hide_widget(splitter):
    sizes = splitter.sizes()
    print("sizes = ", sizes)
    # 如果第二个控件的尺寸小于一个阈值（例如10），则重新显示它
    if sizes[1] < 10:
        # 设置一个最小尺寸来重新显示控件
        splitter.setSizes([100, 100])
# 运行应用程序
app.exec_()
