
import os
import sys

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import PyQt5.QtGui as qg

from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PyQt5.QtGui import QPainter, QPixmap, QWheelEvent
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsPixmapItem,
                             QGraphicsScene, QGraphicsView)



from DesignerUI.PyUI import Ui_Video
from FunctionalUI.VideoAnalysis import video_save
from FunctionalUI.VideoAnalysis import producer

class MyVideo(qw.QMainWindow, Ui_Video.Ui_MainWindow):

    interface_exit_flag = qc.pyqtSignal(bool) # 界面是否存在
    user_exit_flag = qc.pyqtSignal(bool)      # 用户是否存在(是否退出登录等)

    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.resizeToDesktop()
        self.init()

        # self.test()
    
    def init(self):
        # 缩放
        self.zoomInTimes = 0
        self.maxZoomInTimes = 22
        self.AnchorUnderMouse = QGraphicsView.AnchorUnderMouse
        # self.displayedImageSize = QSize(0, 0)
 

        # 为user区域添加按钮
        self.box1_user.setText("已登录!")
        self.login_button = qw.QAction('退出登录', self)
        self.box1_user.addAction(self.login_button)
        self.login_button.triggered.connect(lambda: self.LoginArea(0))

        # 为树形导航绑定槽函数
        self.box2_tree.itemClicked.connect(self.on_box2_tree_cb)

        # 禁止用户操作box5-6
        # self.box5_control.currentChanged.connect(self.on_box5_change_page_cb)
        # self.box6_sub_interface.currentChanged.connect(self.on_box6_change_page_cb)

        self.box5_switch = {
            "图像翻转": 0,
            "提取ROI": 1,
            "编码设置": 2,
            "视频传输": 3,
            "目标检测": 4,
            "场景分割": 5,
            "目标跟踪": 6,
        }
        self.box6_switch = {
            "SubImageDisplay": 0,
            "Console": 1,
        }

        self.box1_clieck_flag = False

        self.save_ui_is_show_flag = False
        self.save_ui = video_save.MySave()
        self.box1_power.clicked.connect(self.on_box1_power_cb)
        self.box1_save.clicked.connect(self.on_box1_save_cb)
        self.save_ui.save_data.connect(self.on_save_ui_show_cb)

        self.GraphicsInit()

        # thread
        self.video_producer = producer.Producer()
        

    def on_box1_power_cb(self):

        if not self.box1_clieck_flag:
            # ret = self.box5_control.setCurrentIndex(0) if self.tt_flag else self.box5_control.setCurrentIndex(1)
            # self.tt_flag = not self.tt_flag
            # print(self.tt_flag)
            # self.video_producer.start()
           
            self.box1_power.setChecked(True)
            self.box1_connection_status.setChecked(True)
        
        else:
            # self.video_producer.stop()
            self.box1_power.setChecked(False)
            self.box1_connection_status.setChecked(False)

        self.box1_clieck_flag = not self.box1_clieck_flag
    def on_box1_save_cb(self):
        if self.save_ui_is_show_flag :
            return
        self.save_ui_is_show_flag = True
        self.save_ui.show()
        
    def on_save_ui_show_cb(self,v_p, v_t, v_m, v_m_d):
        if self.save_ui_is_show_flag:
            self.save_ui_is_show_flag = False
            self.save_ui.close()
            print('1------------------------------------------')
            print(v_p)
            print(v_t)
            print(v_m)
            print(v_m_d)
            print('------------------------------------------')

            

    def on_box2_tree_cb(self, item, column):
        ''' 
            树形导航widget的槽函数绑定 
            item.text(0) 就是对应按钮的汉字
        '''
        print('key = {}\t value = {} column={}'.format(item.text(0), item.text(1), column))
        pass

    def resizeToDesktop(self):
        # desktop 是 QDesktopWidget 对象,他包含了关于屏幕和显示器的信息。
        # : 这一行获取当前应用程序的桌面（desktop）信息
        desktop = QApplication.desktop()

        ## 这一行获取了当前屏幕的可用几何（availableGeometry），也就是除去任务栏等区域之外的屏幕大小
        ## 这个几何对象是一个 QRect，包含了屏幕的左上角坐标以及宽度和高度。
        rect = desktop.availableGeometry(self) 

        ##  这一行设置了窗口的几何形状（位置和大小） 使其等于当前屏幕的可用几何
        self.setGeometry(rect)

    def LoginArea(self, p_enum):
        '''
        # 0:退出登录事件触发
        '''
        u_str = self.box1_user.text()
        if u_str == "已登录!":
            self.box1_user.setText("请登录!")
            self.login_button.setText("点击登录")
            # self.box1_power.setDisabled(False)
        else:
            self.box1_user.setText("已登录!")
            self.login_button.setText("退出登录")
            # self.box1_power.setDisabled(True)
    
    def closeEvent(self, event):
        self.interface_exit_flag.emit(False)
        self.video_producer.stop()
        event.accept()

    def GraphicsInit(self):
        self.AnchorUnderMouse = qw.QGraphicsView.AnchorUnderMouse
        self.graphicsScene = qw.QGraphicsScene()
        # self.box4_graphics.setScene(self.graphicsScene)
    def test(self, frame):
        
        
        
        # self.pixmap = qg.QPixmap(r'C:\Users\12284\Desktop\GitHub\ImageAnalysis\images\img0.jpg')
        self.pixmap = qg.QPixmap(frame)
        self.pixmapItem = qw.QGraphicsPixmapItem(self.pixmap)

        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        # self.box4_graphics.resize(self.box4_graphics.width(), self.box4_graphics.height()) 

        # 隐藏滚动条
        # self.box4_graphics.setVerticalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        # self.box4_graphics.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)

        # 以鼠标所在位置为锚点进行缩放
        self.box4_graphics.setTransformationAnchor(qw.QGraphicsView.AnchorUnderMouse)

        # 平滑缩放
        self.pixmapItem.setTransformationMode(qc.Qt.SmoothTransformation)
        self.box4_graphics.setRenderHints(qg.QPainter.Antialiasing |
                            qg.QPainter.SmoothPixmapTransform)

        # 设置场景

        self.graphicsScene.addItem(self.pixmapItem)
        self.box4_graphics.setScene(self.graphicsScene)
    # --------------------------------------------------------------------------------------- #
    def __isEnableDrag(self):
        """ 根据图片的尺寸决定是否启动拖拽功能 """
        v = self.box4_graphics.verticalScrollBar().maximum() > 0
        h = self.box4_graphics.horizontalScrollBar().maximum() > 0
        return v or h

    def __setDragEnabled(self, isEnabled: bool):
        """ 设置拖拽是否启动 """
        self.box4_graphics.setDragMode(
            self.box4_graphics.ScrollHandDrag if isEnabled else self.box4_graphics.NoDrag)

    def __getScaleRatio(self):
        """ 获取显示的图像和原始图像的缩放比例 """
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width()/pw)
        rh = min(1, self.height()/ph)
        return min(rw, rh)
    def resetTransform(self):
        """ 重置变换 """
        self.box4_graphics.resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)

    def fitInView(self, item: QGraphicsItem, mode=Qt.KeepAspectRatio):
        """ 缩放场景使其适应窗口大小 """
        self.box4_graphics.fitInView(item, mode)
        self.displayedImageSize = self.__getScaleRatio()*self.pixmap.size()
        self.zoomInTimes = 0
    def zoomIn(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 放大图像 """
        if self.zoomInTimes == self.maxZoomInTimes:
            return

        self.box4_graphics.setTransformationAnchor(viewAnchor)

        self.zoomInTimes += 1
        self.box4_graphics.scale(1.1, 1.1)
        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.box4_graphics.setTransformationAnchor(self.AnchorUnderMouse)

    def zoomOut(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 缩小图像 """
        if self.zoomInTimes == 0 and not self.__isEnableDrag():
            return

        self.box4_graphics.setTransformationAnchor(viewAnchor)

        self.zoomInTimes -= 1

        # 原始图像的大小
        pw = self.pixmap.width()
        ph = self.pixmap.height()

        # 实际显示的图像宽度
        w = self.displayedImageSize.width()*1.1**self.zoomInTimes
        h = self.displayedImageSize.height()*1.1**self.zoomInTimes

        
        if pw > self.box4_graphics.width() or ph > self.box4_graphics.height():
            # 在窗口尺寸小于原始图像时禁止继续缩小图像比窗口还小
            if w <= self.box4_graphics.width() and h <= self.box4_graphics.height():
                self.fitInView(self.pixmapItem)
            else:
                self.box4_graphics.scale(1/1.1, 1/1.1)
        else:
            # 在窗口尺寸大于图像时不允许缩小的比原始图像小
            if w <= pw:
                self.box4_graphics.resetTransform()
            else:
                self.box4_graphics.scale(1/1.1, 1/1.1)

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.box4_graphics.setTransformationAnchor(self.AnchorUnderMouse)

    def wheelEvent(self, event):
        self.scale_factor = 1
        delta = event.angleDelta().y()   # 获取滚动方向(向上>0; 向下<0)
        if delta > 0:
            self.zoomIn()  # 放大图像
        else:
            self.zoomOut()  # 缩小图像

    

    