import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 创建一个实时更新的标签
        self.live_label = QLabel("Initial Text")
        self.test_label = QLabel("Initial Text")
        self.statusBar.addWidget(self.live_label)
        self.statusBar.addWidget(self.test_label)

        # 设置一个计时器，每秒更新一次标签内容
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  # 1000毫秒 = 1秒

        self.setWindowTitle('QStatusBar Live Update Example')
        self.resize(400, 200)

    def update_label(self):
        # 更新标签内容为当前时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.live_label.setText(f"Current Time: {current_time}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
