"""
Use a HistogramLUTWidget to control the contrast / coloration of an image.
该代码使用Pyqtgraph库来创建一个图形用户界面GUI，用于展示如何使用直方图查找表LUT来控制图像的对比度和颜色
。pyqtgraph是一个用于科学绘图的python库，他基于pyqt，提供了用于数据可视化和实时数据处理的模块。
"""

import numpy as np

import pyqtgraph as pg  # 绘图库
from pyqtgraph.Qt import QtWidgets # gui库

app = pg.mkQApp("Histogram Lookup Table Example")
win = QtWidgets.QMainWindow()
win.resize(880, 600)
win.show()
win.setWindowTitle('pyqtgraph example: Histogram LUT')

cw = QtWidgets.QWidget()
win.setCentralWidget(cw)

layout = QtWidgets.QGridLayout()
cw.setLayout(layout)
layout.setSpacing(0)

view = pg.GraphicsView()
vb = pg.ViewBox()
vb.setAspectLocked()
view.setCentralItem(vb)
layout.addWidget(view, 0, 1, 3, 1)
# 创建一个 HistogramLUTWidget 他是pyqtgraph库的一个子类,用于显示图像的直方图和Loolup Table(LUT)控制器
# gradientPosition 参数用于指定渐变条（颜色映射）的位置，这里设置为left，意味着渐变条会显示在直方图的左侧
# HistogramLUTWidget 有几个预定义的渐变条位置，包括 “left”, “right”, “top”, 和 “bottom”。 None
hist = pg.HistogramLUTWidget(gradientPosition="None")
layout.addWidget(hist, 0, 2)


monoRadio = QtWidgets.QRadioButton('mono')
rgbaRadio = QtWidgets.QRadioButton('rgba')
layout.addWidget(monoRadio, 1, 2)
layout.addWidget(rgbaRadio, 2, 2)
monoRadio.setChecked(True)


def setLevelMode():
    mode = 'mono' if monoRadio.isChecked() else 'rgba'
    hist.setLevelMode(mode)


monoRadio.toggled.connect(setLevelMode)

# gaussianFilter 对图像进行高斯模糊（一种平滑技术），减少图像噪声和降低细节层次
## np.random.normal(size=(256, 256, 3)) 使用numpy库生成一个特定大小和分布的随机数组
### np.random.normal 用于从正太分布（也称为高斯分布）中抽取随机样本
### size=(256, 256, 3) 表示生成一个256*256*3像素的三维数组
## (20, 20, 0) 表示高斯核的大小和标准差
data = np.random.normal(size=(256, 256, 1))

# 注意上述代码是正态分布啊,所以大部分数据会在 0 附近;通过print(data)发现确实如此
# 如果你不想让你的数据有< 0 的情况 那么可以通过 data = np.clip(data, 0, 255)  # 将数据限制在 0 到 255 的范围内
# data = pg.gaussianFilter(np.random.normal(size=(256, 256, 3)), (20, 20, 0))
for i in range(32):
    for j in range(32):
        data[i*8, j*8] = 255.0
img = pg.ImageItem(data)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(data)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
vb.addItem(img)
vb.autoRange()

hist.setImageItem(img)

if __name__ == '__main__':
    pg.exec()
