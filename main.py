
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

from GuideUI import guide

'''
    vi Ui_Guide.py [+] -> from images import icon_png_rc
    vi Ui_Video.py [+] -> from images import icon_png_rc
    vi Ui_Login.py [+] -> import icon_png_rc
'''

if __name__ == '__main__':
    print('Weclome to MAIN')
    app = qw.QApplication([])
    mainUI = guide.Guide()
    mainUI.show()
    sys.exit(app.exec_())





