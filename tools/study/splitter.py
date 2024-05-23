# 分裂器学习
# https://blog.csdn.net/lg1259156776/article/details/52469244


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSplitter, QTextEdit, QVBoxLayout, QWidget

# 创建一个应用程序实例
app = QApplication(sys.argv)

# 创建两个 QTextEdit 小部件
text_edit1 = QTextEdit()
text_edit2 = QTextEdit()

# 创建一个 QSplitter 实例
splitter = QSplitter()

# 将小部件添加到分割器中
splitter.addWidget(text_edit1)
splitter.addWidget(text_edit2)

# 设置分割器的方向（默认是水平）
splitter.setOrientation(Qt.Horizontal)

# 创建一个主窗口
main_window = QWidget()

# 创建一个垂直布局
layout = QVBoxLayout()

# 将分割器添加到布局中
layout.addWidget(splitter)

# 设置主窗口的布局
main_window.setLayout(layout)

# 显示主窗口
main_window.show()

# 运行应用程序的事件循环
sys.exit(app.exec_())
