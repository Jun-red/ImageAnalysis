import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Widget Example")

        # 创建 Stacked Widget 和两个页面
        self.stacked_widget = QStackedWidget()
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # 创建两个按钮来切换页面
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")
        self.button1.clicked.connect(self.show_page1)
        self.button2.clicked.connect(self.show_page2)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.stacked_widget)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def disable_interactions(self):
        self.stacked_widget.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    # window.disable_interactions()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
