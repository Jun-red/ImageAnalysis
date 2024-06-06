from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QStackedWidget, QHBoxLayout, QApplication, \
    QGridLayout, QPushButton, QLabel, QFrame, QVBoxLayout, QTextBrowser


class StackWindow(QWidget):
    def __init__(self):
        super(StackWindow, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('AutoTest')
        self.resize(1200, 800)

        # 创建列表窗口，添加条目----左侧
        self.leftlist = QListWidget()

        self.test1_leftlist = QListWidgetItem('Test1', self.leftlist)
        # 设置item的默认宽高(这里只有高度比较有用)
        self.test1_leftlist.setSizeHint(QSize(16777215, 100))
        # 文字居中
        self.test1_leftlist.setTextAlignment(Qt.AlignCenter)

        self.test2_leftlist = QListWidgetItem('Test2', self.leftlist)
        self.test2_leftlist.setSizeHint(QSize(16777215, 100))
        self.test2_leftlist.setTextAlignment(Qt.AlignCenter)
        self.test2_leftlist.setHidden(True)  # 隐藏

        self.test3_leftlist = QListWidgetItem('Test3', self.leftlist)
        self.test3_leftlist.setSizeHint(QSize(16777215, 100))
        self.test3_leftlist.setTextAlignment(Qt.AlignCenter)
        self.test3_leftlist.setHidden(True)  # 隐藏

        # 去掉边框
        self.leftlist.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.leftlist.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.leftlist.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 创建三个控件----右侧（左右对应）
        self.stack_1 = QWidget()
        self.stack_1.setObjectName('stack_1')
        self.stack_2 = QWidget()
        self.stack_2.setObjectName('stack_2')
        self.stack_3 = QWidget()
        self.stack_3.setObjectName('stack_3')

        self.stack_1UI()
        self.stack_2UI()
        self.stack_3UI()

        # 在QStackWidget对象中填充三个子控件
        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack_1)
        self.stack.addWidget(self.stack_2)
        self.stack.addWidget(self.stack_3)

        # 水平布局，添加部件到布局中
        hbox = QHBoxLayout()
        hbox.setObjectName('hbox')
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        self.leftlist.currentRowChanged.connect(self.display)

    def stack_1UI(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName('grid_layout')

        self.click_button = QPushButton()
        self.click_button.setObjectName("click_button")
        self.click_button.setText("请点击")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(30)
        self.click_button.setFont(font)
        self.click_button.clicked.connect(self.show_2_3)
        self.grid_layout.addWidget(self.click_button, 0, 0, 2, 2)

        self.label_1 = QLabel()
        self.label_1.setObjectName('label_1')
        font = QtGui.QFont()
        font.setFamily('楷体')
        font.setBold(True)
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setText('这是页面1')
        self.grid_layout.addWidget(self.label_1, 2, 0, 1, 1)
        self.stack_1.setLayout(self.grid_layout)

    def stack_2UI(self):
        self.grid2_layout = QGridLayout()
        self.grid2_layout.setObjectName('grid2_layout')   # 整个页面二的格栅布局
        self.hbox_update = QHBoxLayout()
        self.hbox_update.setObjectName('hbox_update')   # 格栅布局里的水平布局（布局嵌套）
        self.label = QLabel()
        self.label.setText('这是页面2:')
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(20)
        self.label.setFont(font)
        self.hbox_update.addWidget(self.label)

        self.click_button_2 = QPushButton()
        self.click_button_2.setObjectName('click_button_2')
        self.click_button_2.setText('请点击，效果只有一次')
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(20)
        self.click_button_2.setFont(font)
        self.click_button_2.setStyleSheet(
            '''QRadioButton{background:#CFCFCF;border-radius:5px;}QRadioButton:hover{background:yellow;}''')
        self.click_button_2.clicked.connect(self.text_show)
        self.hbox_update.addWidget(self.click_button_2)   # 如果有多少个控件添加多少个

        self.grid2_layout.addLayout(self.hbox_update, 0, 0, 1, 1)   # （布局嵌套）

        # 可隐藏布局----布局不能直接隐藏，采用QFrame对象的间接方式隐藏
        self.layout_hide = QFrame()   # 先设置一个QFrame对象
        self.layout_hide.setObjectName('layout_hide')
        self.layout_hide.setFrameShape(QFrame.StyledPanel)
        self.layout_hide.hide()    # 让QFrame对象隐藏
        self.horizontalLayout = QVBoxLayout(self.layout_hide)   # 垂直布局---该布局可隐藏，因为有QFrame对象
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.textB = QTextBrowser()
        self.textB.setObjectName('textB')
        self.textB.setText('已显示')
        self.textB.setFont(font)
        self.horizontalLayout.addWidget(self.textB)

        # 代码1和代码2两行代码有无效果不同，可自行查看
        self.grid2_layout.addWidget(self.layout_hide, 1, 0, 1, 1)     # 代码1
        self.grid2_layout.addLayout(self.horizontalLayout, 1, 0, 1, 1)   # 代码2

        self.stack_2.setLayout(self.grid2_layout)

    def stack_3UI(self):
        self.grid3_layout = QGridLayout()
        self.grid3_layout.setObjectName('grid2_layout')

        self.label_2 = QLabel()
        self.label_2.setObjectName('label_2')
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)   # 文字居中
        self.label_2.setText('这是页面3')
        self.grid3_layout.addWidget(self.label_2, 0, 0, 1, 2)

        self.stack_3.setLayout(self.grid3_layout)

    def show_2_3(self):
        self.test2_leftlist.setHidden(False)
        self.test3_leftlist.setHidden(False)

    def text_show(self):
        self.layout_hide.show()

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)

# qss
Stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    font-size: 24px;
    background: rgb(192, 192, 192);
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(192, 192, 192);
}

"""

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    demo = StackWindow()
    demo.show()
    sys.exit(app.exec_())
