# 实现鼠标移动控件上的弹窗显示
## https://cloud.tencent.com/developer/article/1344572
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import PyQt5.QtGui as qg
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QVBoxLayout, QWidget, QMenuBar, QToolBar, QAction
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DockWidget with Menu and Toolbar")
        self.resize(800, 600)

        # 创建主控件
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # 创建左上角的按钮
        self.toggle_button = qw.QPushButton("Toggle Sidebar")
        self.toggle_button.clicked.connect(self.toggle_sidebar)
        self.main_layout.addWidget(self.toggle_button)

        # 创建QDockWidget
        self.dock_widget = QDockWidget("Sidebar", self)
        self.dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # 创建一个子控件来容纳菜单栏和工具栏
        self.dock_content = QWidget()
        self.dock_layout = QVBoxLayout(self.dock_content)

        # 创建菜单栏
        self.menu_bar = QMenuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.dock_layout.addWidget(self.menu_bar)

        # 添加菜单项
        self.file_menu.addAction(QAction("New", self))
        self.file_menu.addAction(QAction("Open", self))
        self.edit_menu.addAction(QAction("Undo", self))
        self.edit_menu.addAction(QAction("Redo", self))

        # 创建工具栏
        self.tool_bar = QToolBar()
        self.tool_bar.addAction(QAction("New", self))
        self.tool_bar.addAction(QAction("Open", self))
        self.dock_layout.addWidget(self.tool_bar)

        # 添加内容区域
        self.text_edit = QTextEdit()
        self.dock_layout.addWidget(self.text_edit)

        self.dock_widget.setWidget(self.dock_content)

        # 将QDockWidget添加到主窗口的左侧
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)

        # 标记当前边栏状态
        self.is_sidebar_expanded = True

        # 存储原始宽度
        self.original_width = self.dock_widget.width()

    def toggle_sidebar(self):
        if self.is_sidebar_expanded:
            self.original_width = self.dock_widget.width()  # 存储当前宽度
            self.dock_widget.setMaximumWidth(30)  # 设置为仅显示一小部分
            self.dock_widget.setMinimumWidth(30)
        else:
            self.dock_widget.setMaximumWidth(self.original_width)  # 恢复原始宽度
            self.dock_widget.setMinimumWidth(self.original_width)
        self.is_sidebar_expanded = not self.is_sidebar_expanded

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
