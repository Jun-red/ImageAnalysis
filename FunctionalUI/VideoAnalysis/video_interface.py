
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

class MyVideo(qw.QMainWindow, Ui_Video.Ui_MainWindow):

    interface_exit_flag = qc.pyqtSignal(bool) # 界面是否存在
    user_exit_flag = qc.pyqtSignal(bool)      # 用户是否存在(是否退出登录等)

    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.init()

        self.test()
    
    def init(self):

        # 为user区域添加按钮
        self.box1_user.setText("已登录!")
        self.login_button = qw.QAction('退出登录', self)
        self.box1_user.addAction(self.login_button)
        self.login_button.triggered.connect(lambda: self.LoginArea(0))

        # 为设备连接更改图标
        self.box1_connection_status.setDisabled(False) # 默认是断开状态

        # 为开始操作/结束操作更改图标
        self.box1_power.setDisabled(False)

    def test(self):

        t_h = self.box4_graphics.geometry()
        print(t_h.x())
        print(t_h.y())
        print(t_h.width())
        print(t_h.height())

        self.zoomInTimes = 0
        self.maxZoomInTimes = 22
        self.AnchorUnderMouse = qw.QGraphicsView.AnchorUnderMouse

        self.graphicsScene = qw.QGraphicsScene()
        # self.pixmap = qg.QPixmap(r'images\img0.jpg')
        # self.pixmapItem = qw.QGraphicsPixmapItem(self.pixmap)
        self.setImage(r'images\img0.jpg')
        self.displayedImageSize = qc.QSize(0, 0)
        """ 初始化小部件 """
        self.box4_graphics.resize(self.box4_graphics.width(), self.box4_graphics.height()) 

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
        event.accept()

    # --------------------------------------------------------------------------------------- #
    def wheelEvent(self, e: QWheelEvent):
        """ 滚动鼠标滚轮缩放图片 """
        if e.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def resizeEvent(self, e):
        """ 缩放图片 """
        self.box4_graphics.resizeEvent(e)

        if self.zoomInTimes > 0:
            return

        # 调整图片大小
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

    def setImage(self, imagePath: str):
        """ 设置显示的图片 """
        self.resetTransform()

        # 刷新图片
        self.pixmap = QPixmap(r'images\img0.jpg')
        self.pixmapItem = qw.QGraphicsPixmapItem(self.pixmap)
        # self.pixmapItem.setPixmap(self.pixmap)

        # 调整图片大小
        self.box4_graphics.setSceneRect(QRectF(self.pixmap.rect()))
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)

    def resetTransform(self):
        """ 重置变换 """
        self.box4_graphics.resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)

    def __isEnableDrag(self):
        """ 根据图片的尺寸决定是否启动拖拽功能 """
        v = self.box4_graphics.verticalScrollBar().maximum() > 0
        h = self.box4_graphics.horizontalScrollBar().maximum() > 0
        return v or h

    def __setDragEnabled(self, isEnabled: bool):
        """ 设置拖拽是否启动 """
        self.box4_graphics.setDragMode(
            self.ScrollHandDrag if isEnabled else self.box4_graphics.NoDrag)

    def __getScaleRatio(self):
        """ 获取显示的图像和原始图像的缩放比例 """
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width()/pw)
        rh = min(1, self.height()/ph)
        return min(rw, rh)

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

        if pw > self.width() or ph > self.height():
            # 在窗口尺寸小于原始图像时禁止继续缩小图像比窗口还小
            if w <= self.width() and h <= self.height():
                self.fitInView(self.pixmapItem)
            else:
                self.box4_graphics.scale(1/1.1, 1/1.1)
        else:
            # 在窗口尺寸大于图像时不允许缩小的比原始图像小
            if w <= pw:
                self.resetTransform()
            else:
                self.box4_graphics.scale(1/1.1, 1/1.1)

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.box4_graphics.setTransformationAnchor(self.AnchorUnderMouse)
    

# if __name__ == '__main__':
#     print("hello World")