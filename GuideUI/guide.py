import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

from DesignerUI.PyUI import Ui_Guide
from GuideUI.LoginUI import login
from FunctionalUI.VideoAnalysis import video_interface

from common import TimeChange
from script import mygit


class Guide(qw.QMainWindow, Ui_Guide.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        self.login = login.Login()
        self.video = video_interface.MyVideo()
        self.function_set= [0] * 5 # video image lidar serial network         

        self.guide_switch = {
            0: self.on_guide_home_cb,
            1: self.on_guide_user_cb,
            2: self.on_guide_github_cb,
            3: self.on_guide_phone_cb,
            4: self.on_guide_power_cb,
        }

        self.CB()
        self.Init()
        self.resizeToDesktop()

    def resizeToDesktop(self):
        desktop = qw.QApplication.desktop()
        rect = desktop.availableGeometry(self) 
        new_width = rect.width() // 1.5
        new_height = rect.height() // 1.5
        self.setGeometry(rect.x(), rect.y(), new_width, new_height)

    def Init(self):
        self.guide_user_login.setStyleSheet("background-color: red;")
        self.guide_user_login.setText("点击登录")

        repo_path = r'C:\Users\12284\Desktop\GitHub\ImageAnalysis'
        branch_name = 'ui_dev'
        changelog_path = r'C:\Users\12284\Desktop\GitHub\ImageAnalysis\ChangeLog.md'
        self.mygit = mygit.MyGitManager(repo_path, branch_name, changelog_path)

        # self.guide_github_url.setText(str(self.mygit.repo_path))
        self.guide_github_branch.setText(str(self.mygit.branch_name))
        self.guide_github_version.setText(str(self.mygit.changelog))
        


    def CB(self):
        self.guide.currentChanged.connect(self.on_guide_cb)

        self.guide_video.clicked.connect(self.on_guide_video_cb)
        self.guide_image.clicked.connect(self.on_guide_image_cb)
        self.guide_netword.clicked.connect(self.on_guide_network_cb)
        self.guide_lidar.clicked.connect(self.on_guide_lidar_cb)
        self.guide_serial.clicked.connect(self.on_guide_serial_cb)

        self.guide_user_login.clicked.connect(self.on_guide_user_login_in_cb)
        self.login.login_flag.connect(self.on_guide_flag_cb)
        self.login.login_time.connect(self.on_guide_time_cb)

        self.video.interface_exit_flag.connect(self.on_video_interface_exit_cb)
    def on_guide_cb(self):
        cur_tab = self.guide.currentIndex()
        self.guide_switch.get(cur_tab)()

    # < 导航界面--Guide-UI > #
    def on_guide_home_cb(self):
        pass
    def on_guide_user_cb(self):
        pass
    def on_guide_github_cb(self):
        print("on_guide_github_cb")
    def on_guide_phone_cb(self):
        print("on_guide_phone_cb")
    def on_guide_power_cb(self):
        print("on_guide_power_cb")
    
    # < tab1 > # 
    def FunctionClickedEvent(self):
        ret = False
        if not self.login.flag :
            qw.QMessageBox.critical(None, "ERROR", "请先完成登录!", qw.QMessageBox.Ok)
            self.function_set = [0 for _ in self.function_set]
        elif sum(self.function_set) != 0:
            qw.QMessageBox.critical(None, "ERROR", "后台已有服务开启", qw.QMessageBox.Ok)
        else:
            ret = not ret
        return ret
    def on_guide_video_cb(self):
        ### DEBUG 模式 先无需登录
        # if  not self.FunctionClickedEvent():
        #     return
        # else:
        #     self.function_set[0] = 1
        #     self.video.show()
        self.video.show()
        try:
            self.video.Start()
        except:
            print("尝试打开线程失败")
            pass

    def on_guide_image_cb(self):
        if  not self.FunctionClickedEvent():
            return
        else:
            self.function_set[1] = 1
    def on_guide_network_cb(self):
        if  not self.FunctionClickedEvent():
            return
        else:
            self.function_set[2] = 1
    def on_guide_lidar_cb(self):
        if  not self.FunctionClickedEvent():
            return
        else:
            self.function_set[3] = 1
    def on_guide_serial_cb(self):
        if  not self.FunctionClickedEvent():
            return
        else:
            self.function_set[4] = 1
    
    # <tab 2> #
    def on_guide_user_login_in_cb(self):
        if self.login.flag:
            self.guide_user_login.setStyleSheet("background-color: red;")
            self.guide_user_login.setText("点击登录")
            self.login.close()
            self.login.flag = False
        else:
            self.login.show()
    def on_guide_flag_cb(self, value):
        if value:
            self.guide_user_login.setText("退出登录")
            self.guide_user_login.setStyleSheet("background-color: green;")
            self.guide_user_name.setText(self.login.login_user_name)
            self.login.close()
    def on_guide_time_cb(self, value):
        str_time = TimeChange.seconds_to_hms(value)
        self.guide_user_time.setText(str_time)
    
    # <Video 功能区域>
    def on_video_interface_exit_cb(self, value):
        ''' 界面关闭了 '''
        if not value:
            self.function_set[0] = 0