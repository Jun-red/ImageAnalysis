"""
Use a HistogramLUTWidget to control the contrast / coloration of an image.
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

# app = pg.mkQApp("Histogram Lookup Table Example")
# win = QtWidgets.QMainWindow() # 创建一个QMainWindow对象,这是GUI的主窗口
# win.resize(880, 600) # 调整窗口的大小为 880 * 600
# win.show() # 显示窗口
# win.setWindowTitle('pyqtgraph example: Histogram LUT') # 设置窗口的标题

# cw = QtWidgets.QWidget() # 创建一个QWidget对象，他将被设置为窗口的中央部件
# win.setCentralWidget(cw) # 将QWidget设置为 GUI主窗口的中央部件

# layout = QtWidgets.QGridLayout() # 用于布局cw中的控件
# cw.setLayout(layout) # 将layout设置为cw的布局
# layout.setSpacing(0) # 设置布局中的控件间距为0

# view = pg.GraphicsView() # 创建一个GraphicsView对象，用于显示图形
# vb = pg.ViewBox()
# vb.setAspectLocked()
# view.setCentralItem(vb)
# layout.addWidget(view, 0, 1, 3, 1) # 将view添加到布局的第0行第1列;占据3行1列的空间

# hist = pg.HistogramLUTWidget(gradientPosition="left") # 用于显示直方图和LUT(look-up table)
# layout.addWidget(hist, 0, 2) # 将hist添加到布局的第0行第2列


# monoRadio = QtWidgets.QRadioButton('mono')
# rgbaRadio = QtWidgets.QRadioButton('rgba')
# layout.addWidget(monoRadio, 1, 2)
# layout.addWidget(rgbaRadio, 2, 2)
# monoRadio.setChecked(True)


# def setLevelMode():
#     mode = 'mono' if monoRadio.isChecked() else 'rgba'
#     hist.setLevelMode(mode)


# monoRadio.toggled.connect(setLevelMode)

# data = pg.gaussianFilter(np.random.normal(size=(256, 256, 3)), (20, 20, 0))
# for i in range(32):
#     for j in range(32):
#         data[i*8, j*8] += .1
# img = pg.ImageItem(data)
# vb.addItem(img)
# vb.autoRange()

# hist.setImageItem(img)

# if __name__ == '__main__':
#     pg.exec()
import sys
import cv2
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# class ImageViewer(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Image Viewer with Histogram and LUT')
#         self.setGeometry(100, 100, 800, 600)

#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)

#         # Image view widget
#         self.image_view = pg.ImageView()
#         layout.addWidget(self.image_view)

#         # HistogramLUT widget
#         self.histogram_lut = pg.HistogramLUTWidget()
#         layout.addWidget(self.histogram_lut)

#         # Load image
#         self.image = cv2.imread(r'C:\Users\12284\Desktop\GitHub\ImageAnalysis\tools\study\china.png', cv2.IMREAD_GRAYSCALE)
#         if self.image is None:
#             raise Exception("Image not found or unable to load.")

#         # Display image
#         self.image_view.setImage(self.image)
        
#         # Connect HistogramLUTWidget to ImageView
#         self.histogram_lut.setImageItem(self.image_view.getImageItem())

# def main():
#     app = QApplication(sys.argv)
#     viewer = ImageViewer()
#     viewer.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

"""
Demonstrates common image analysis tools.

Many of the features demonstrated here are already provided by the ImageView
widget, but here we present a lower-level approach that provides finer control
over the user interface.
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

# 翻译 # 将图像数据解释为以行为主而不是以列为主
# Interpret image data as row-major instead of col-major
pg.setConfigOptions(imageAxisOrder='row-major')

pg.mkQApp()
win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Image Analysis')

# A plot area (ViewBox + axes) for displaying the image
p1 = win.addPlot(title="")

# Item for displaying image data
img = pg.ImageItem()
p1.addItem(img)

# Custom ROI for selecting an image region
roi = pg.ROI([-8, 14], [6, 5])
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
p1.addItem(roi)
roi.setZValue(10)  # make sure ROI is drawn above image

# Isocurve drawing
iso = pg.IsocurveItem(level=0.8, pen='g')
iso.setParentItem(img)
iso.setZValue(5)

# Contrast/color control
hist = pg.HistogramLUTItem()
hist.setImageItem(img)
win.addItem(hist)

# Draggable line for setting isocurve level
isoLine = pg.InfiniteLine(angle=0, movable=True, pen='g')
hist.vb.addItem(isoLine)
hist.vb.setMouseEnabled(y=False) # makes user interaction a little easier
isoLine.setValue(0.8)
isoLine.setZValue(1000) # bring iso line above contrast controls

# Another plot area for displaying ROI data
win.nextRow()
p2 = win.addPlot(colspan=2)
p2.setMaximumHeight(250)
win.resize(800, 800)
win.show()


# Generate image data
data = np.random.normal(size=(200, 100))
data[20:80, 20:80] += 2.
data = pg.gaussianFilter(data, (3, 3))
data += np.random.normal(size=(200, 100)) * 0.1
img.setImage(data)
hist.setLevels(data.min(), data.max())

# build isocurves from smoothed data
iso.setData(pg.gaussianFilter(data, (2, 2)))

# set position and scale of image
tr = QtGui.QTransform()
img.setTransform(tr.scale(0.2, 0.2).translate(-50, 0))

# zoom to fit imageo
p1.autoRange()  


# Callbacks for handling user interaction
def updatePlot():
    global img, roi, data, p2
    selected = roi.getArrayRegion(data, img)
    p2.plot(selected.mean(axis=0), clear=True)

roi.sigRegionChanged.connect(updatePlot)
updatePlot()

def updateIsocurve():
    global isoLine, iso
    iso.setLevel(isoLine.value())

isoLine.sigDragged.connect(updateIsocurve)

def imageHoverEvent(event):
    """Show the position, pixel, and value under the mouse cursor.
    """
    if event.isExit():
        p1.setTitle("")
        return
    pos = event.pos()
    i, j = pos.y(), pos.x()
    i = int(np.clip(i, 0, data.shape[0] - 1))
    j = int(np.clip(j, 0, data.shape[1] - 1))
    val = data[i, j]
    ppos = img.mapToParent(pos)
    x, y = ppos.x(), ppos.y()
    p1.setTitle("pos: (%0.1f, %0.1f)  pixel: (%d, %d)  value: %.3g" % (x, y, i, j, val))

# Monkey-patch the image to use our custom hover function. 
# This is generally discouraged (you should subclass ImageItem instead),
# but it works for a very simple use like this. 
img.hoverEvent = imageHoverEvent

if __name__ == '__main__':
    # pg.exec()

    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    # 读取图像
    image = cv2.imread(r'C:\Users\12284\Desktop\GitHub\ImageAnalysis\images\china.png', cv2.IMREAD_GRAYSCALE)

    # 计算直方图
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 绘制直方图
    plt.plot(hist, color='black')
    plt.title('Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.show()

