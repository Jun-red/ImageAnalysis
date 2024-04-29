import sys

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

from DesignerUI.PyUI import Ui_Login

class Login(qw.QMainWindow, Ui_Login.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # setupUi表示当前界面的控件都属于当前对象



# if __name__ == '__main__':
#     print('Weclome to Login')

