# QDockWidget类提供了一个可以停靠在QMainWindow中或作为桌面上的顶级窗口浮动的部件。
# 注意: 当前父控件一定是QMainWindow
# https://www.bilibili.com/video/BV1p64y1t7yD/?spm_id_from=333.337.search-card.all.click&vd_source=ad3084bd3bd6a946d53699f12e28764d
# https://www.cnblogs.com/LaoYuanPython/p/12634949.html

# QT 官方文档
## https://doc.qt.io/qt-5/qwidget.html#minimumSizeHint-prop

# 以下代码主要用于实现dock的比例控制

'''
在 Qt 中，特别是使用 QMainWindow 时，这些属性与窗口中的停靠窗口（docks）的行为有关。以下是每个属性的解释：

AnimatedDocks：
    这个属性决定了停靠窗口的动画效果是否启用。当设置为 true 时，停靠窗口的移动和改变大小将会显示动画效果，
这通常会提供更平滑的用户体验。
AllowNestedDocks：
    这个属性决定了停靠窗口是否可以嵌套。如果设置为 true，则可以将一个停靠窗口停靠在另一个停靠窗口内，形成嵌套结构。
如果设置为 false，则停靠窗口不能嵌套，只能直接停靠在主窗口的边缘或中心区域。
ForceTabbedDocks：
    当这个属性设置为 true 时，所有停靠的窗口都会被组织成标签页形式，即使它们没有被拖动到一起。这意味着用户无法将停靠窗口分离出来，
它们总是以标签页的形式存在。
VerticalTabs：
    这个属性仅当停靠窗口以标签页形式存在时有效。如果设置为 true，则标签页将会垂直排列，而不是默认的水平排列。
GroupedDragging：
    当这个属性设置为 true 时，用户可以拖动一个停靠窗口组（即一个包含多个标签页的停靠窗口）到另一个停靠窗口或主窗口的中央区域。
如果设置为 false，则用户只能拖动单个停靠窗口，而不能拖动整个组。这些属性通常在 QMainWindow 的构造函数中设置，或者在创建
主窗口之后的某个时刻设置，以控制停靠窗口的行为和外观。通过组合使用这些属性，开发者可以创建具有不同布局和行为的自定义应用程序界面。

'''

''' 
    如何设置dock的比例呢?比如有三个垂直布局的dock,如何预设比例呢?
    1. 在UI中,好像不能设置.因为mainwindow会自动的设置，调整
    2. 当然在显示的时候，可以手动拖动（将鼠标移动到两个dock之间就会出现一个控制大小的抓手）
    3. 貌似是设计UI的时候，可以将A (A,B,C)中的子控件设置的小一点，dock-B中的子控件大一些就可以

    参考:
    https://www.coder.work/article/7937377
'''

import sys
from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QSplitter, QTextEdit, QVBoxLayout, QWidget,QDockWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QSplitter, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个 QSplitter
        splitter = QSplitter()

        # 创建三个停靠窗口
        dock1 = QDockWidget("Dock 1", self)
        dock2 = QDockWidget("Dock 2", self)
        dock3 = QDockWidget("Dock 3", self)

        # 创建三个简单的 QWidget 作为停靠窗口的内容
        widget1 = QWidget()
        widget2 = QWidget()
        widget3 = QWidget()

        # 将 QWidget 添加到停靠窗口
        dock1.setWidget(widget1)
        dock2.setWidget(widget2)
        dock3.setWidget(widget3)

        # # 将停靠窗口添加到 QSplitter
        # splitter.addWidget(dock1)
        # splitter.addWidget(dock2)
        # splitter.addWidget(dock3)

        # # 设置 QSplitter 的布局方向为垂直
        # splitter.setOrientation(Qt.Vertical)

        # # 设置停靠窗口的比例
        # splitter.setSizes([100, 300, 200])

        # 将 QSplitter 设置为中心小部件
        # self.setCentralWidget(splitter)

        # 显示窗口
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
