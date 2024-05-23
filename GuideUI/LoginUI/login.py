import sys

# from PyQt5.QtCore import QObject, pyqtSignal
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

from DesignerUI.PyUI import Ui_Login


class Login(qw.QMainWindow, Ui_Login.Ui_Form):
    login_flag = qc.pyqtSignal(bool)
    login_time = qc.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.flag = False
        self.login_in.clicked.connect(self.on_login_in_cb)
        self.login_register.clicked.connect(self.on_login_register_cb)

        # self.login_user_name = ""
        # self.login_user_passworld = ""
    
    def StartTimer(self, timeout):
        # self.timer = qc.QTimer(self)
        # self.timer.timeout.connect(self.UpdateTimer) 
        # self.timer.start(timeout)  # 每隔1000毫秒（即1秒）触发一次定时器
        self.counter = 0 
    
    def UpdateTimer(self):
        self.counter += 1
        self.login_time.emit(self.counter)
    def closeEvent(self, event):
        try:
            self.timer.close()
        except:
            pass
        event.accept()
        
    def on_login_in_cb(self):
        if self.login_name.text() == "root":
            if self.login_password.text() == "root":
                self.flag = True
                self.login_user_name = self.login_name.text()
                self.login_user_passworld = self.login_password.text()
                self.login_name.clear()
                self.login_password.clear()
                self.login_flag.emit(True)
                self.StartTimer(1000)
            else:
                self.login_password.clear()
        else:
            self.login_name.clear()
            self.login_password.clear()
    def on_login_register_cb(self):
        pass
# if __name__ == '__main__':
#     print('Weclome to Login')

