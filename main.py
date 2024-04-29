
import sys
import os

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJ_DIR)
sys.path.append(os.path.join(PROJ_DIR, 'common'))
sys.path.append(os.path.join(PROJ_DIR, 'DesignerUI'))
sys.path.append(os.path.join(PROJ_DIR, 'FunctionalUI'))
sys.path.append(os.path.join(PROJ_DIR, 'GuideUI'))
sys.path.append(os.path.join(PROJ_DIR, 'script'))
sys.path.append(os.path.join(PROJ_DIR, 'tools'))
sys.path.append(os.path.join(PROJ_DIR, 'images'))

from GuideUI.LoginUI import login

class Guide(qw.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)  

        self.login = login.Login()


if __name__ == '__main__':
    print('Weclome to MAIN')
    app = qw.QApplication([])

    mainUI = Guide()
    mainUI.login.show()
    # mainUI.show()

    sys.exit(app.exec_())
