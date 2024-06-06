"""
Demonstrates common image analysis tools.

Many of the features demonstrated here are already provided by the ImageView
widget, but here we present a lower-level approach that provides finer control
over the user interface.
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

# Interpret image data as row-major instead of col-major
pg.setConfigOptions(imageAxisOrder='row-major')
# mkQApp 是  pyqtgraph库中的一个辅助函数  用于创建一个QApplication实例. 
# QApplication 是pyqt或pyside应用程序的基础，他管理应用程序的控制流和主要设置，是GUI应用程序与用户交互的核心
# 在pyqt或pyside应用程序中，通常只需要一个 QApplication实例. pyqtgraph.mkQApp() 函数检查是否已经存在一个
#  QApplication 实例，如果不存在，则创建一个新的实例。如果已经存在，它将返回现有的实例。这样可以确保在
# 多模块应用程序中不会创建多个 QApplication 实例，从而避免潜在的问题。
pg.mkQApp()
# GraphicsLayoutWidget 是一个用于布局和显示图形项（如图像、图表、文本等）的容器。
# GraphicsLayoutWidget 提供了灵活的布局系统，允许图形项以网格形式排列
win = pg.GraphicsLayoutWidget() 
win.setWindowTitle('pyqtgraph example: Image Analysis') # 设置窗口标题

## 在 GraphicsLayoutWidget 控件中添加一个新的绘图区域(addPlot方法返回一个PlotItem实例)
## 该实例可以用来显示图像、图表等
# A plot area (ViewBox + axes) for displaying the image
p1 = win.addPlot(title="")

# Item for displaying image data
img = pg.ImageItem() # 创建一个ImageItem实例，用于显示图像数据
p1.addItem(img) # 将img嵌合到PlotItem中，这样图像就可以在PlotItem提供的坐标系中显示

# 创建一个ROI实例，他允许用户通过拖动来选择图像的一个区域
# ROI的初始位置由两个参数指定：第一个参数是ROI的左上角坐标； 第二个参数是ROI的宽度和高度
# Custom ROI for selecting an image region 用于选择图像区域的自定义 ROI
roi = pg.ROI([-8, 14], [6, 5])
# 以下两句添加了缩放手柄到ROI，允许用户通过拖动手柄来改变ROI的大小，每个手柄的位置和方向由两个参数指定：
## 第一个参数是手柄相对于ROI的位置； 第二个参数是手柄的方向
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
# 将roi添加到PlotItem中，使其显示在图像上
p1.addItem(roi)
# 这行代码设置了ROI的Z值（深度值），Z值较高的绘图项会绘制在Z值较低的绘图项上。
roi.setZValue(10)  # make sure ROI is drawn above image

# IsocurveItem(等值线项) 用于绘制等高线(就是类似山丘那种),将大于>pixel_value的部分圈出来
# level是等高线的阈值，pen参数指定了绘制等高线的颜色（这里为绿色）
# Isocurve drawing
iso = pg.IsocurveItem(level=0.8, pen='g')
# 将等高线的父项设置为ImageItem  这样等高线会随着图像的缩放和平移而相应的调整
iso.setParentItem(img)
# 设置等高线的Z值，确保等高线在图像下方但在ROI上方绘制
iso.setZValue(5)

## 创建一个 HistogramLUTItem 实例，用于显示图像的直方图和Looup Table(LUT),允许用户调整图像的对比度和颜色
# Contrast/color control
hist = pg.HistogramLUTItem()
## 将 HistogramLUTItem 关联到 ImageItem(img)，这样直方图和LUT控制器就会根据图像数据更新
hist.setImageItem(img)
# 将 hist控件添加到 GraphicsLayoutWidget(win)中，使其显示在窗口中
win.addItem(hist)

# Draggable line for setting isocurve level 可拖动线用于设置等高线级别
## 创建一个 InfiniteLine 实例,他是一个垂直的（因为angle=0）可拖动的线条，用于设置等高线的水平
isoLine = pg.InfiniteLine(angle=0, movable=True, pen='g')
## 将InfiniteLine线条添加到直方图的视图框(vb)中，使其显示在直方图的旁边
hist.vb.addItem(isoLine)
# 这行代码禁用了直方图视图框的垂直鼠标交互，这样用户用户就只能通过水平拖动来调整对比度了，而不能垂直拖动
hist.vb.setMouseEnabled(y=False) # makes user interaction a little easier
isoLine.setValue(0.8) # 设置了 InfiniteLine 的初始值，即等高线的初始阈值。
# 这行代码设置了 InfiniteLine 的 Z 值，确保它显示在对比度控制之上。
isoLine.setZValue(1000) # bring iso line above contrast controls

# Another plot area for displaying ROI data # 另一个用于显示 ROI 数据的绘图区域
#  这行代码将图形布局窗口的当前行推进到下一行，为添加新的绘图区域做准备。
win.nextRow()
#  这行代码在新的行中添加了一个新的绘图区域  colspan=2 表示 它占据了两列的空间。
p2 = win.addPlot(colspan=2)
#  这行代码设置了 p2 的高度限制，使其最大高度为 250 像素。
p2.setMaximumHeight(250)
# 这行代码调整了图形布局窗口的大小，使其宽度和高度都为 800 像素。
win.resize(800, 800)
# win.show() 这行代码显示了图形布局窗口及其所有子项。
win.show()

# --------------------------------  上上述代码实现的是 控件创建/初始化/控件位置安排 ---
# --------------------------------  下面代码实现 图像生成、roi直方图显示等实时变化数据 ---

# Generate image data 生成图像数据
## 使用numpy生成一个200*100像素的随机高斯噪声图像数据
data = np.random.normal(size=(200, 100))
## 这行代码在图像数据的一个区域中增加了一个常数，创建了一个常亮区域
data[20:80, 20:80] += 2.
# 使用高斯滤波函数对图像进行平滑处理
data = pg.gaussianFilter(data, (3, 3))
# 向图像数据添加了额外的随机噪声
data += np.random.normal(size=(200, 100)) * 0.1
# 将生成的data 设置到ImageItem中，以在界面上显示
img.setImage(data)
# 设置了直方图的显示级别，即图像数据的最大值和最小值
hist.setLevels(data.min(), data.max())

# build isocurves from smoothed data 根据平滑数据构建等值线
## 根据实践，iso是选择等高线区域的，但是等高线区域的边缘线是非平滑的
# 因此 gaussianFilter 是对等高线的边缘线进行平滑的 ，如果不想平滑，那么直接iso.setData(data)
# iso.setData(data)
iso.setData(pg.gaussianFilter(data, (2, 2))) 

# set position and scale of image   设置图像的位置和比例
tr = QtGui.QTransform() # 创建一个QTransform实例，用于定义图像的变换
# 这行代码对图像应用了一个缩放和平移变换，使其在视图中的大小和位置适合。
img.setTransform(tr.scale(0.2, 0.2).translate(-50, 0)) 

# zoom to fit imageo
## 自动 调整 p1 绘图区域的视图范围，以确保图像完全显示在绘图区域内
p1.autoRange()  

# --------------------------------  上上述代码实现 图像生成、roi直方图显示等实时变化数据---
# --------------------------------  下面代码绑定响应事件，比如ROI区域变化、等高线阈值变化，LUT变化 ---


# Callbacks for handling user interaction
def updatePlot():
    global img, roi, data, p2
    # getArrayRegion 方法来获取图像数据中的ROI所选区域的数组,selected是numpy数组
    selected = roi.getArrayRegion(data, img)
    # 在p2绘图区域绘制ROI区域的平均值， selected.mean(axis=0) 计算沿着第一个轴(列)的平均值
    print("==========================")
    print(selected)
    print("==========================")
    # clear=True表示在绘制数据之前先清除之前的绘图
    ttt = selected.mean(axis=0)
    print(ttt)
    print("EE==========================")
    p2.plot(selected.mean(axis=0), clear=True)
# 每当ROI区域改变时，都会响应事件
roi.sigRegionChanged.connect(updatePlot)
updatePlot()

def updateIsocurve():
    global isoLine, iso
    iso.setLevel(isoLine.value())
# 每当用户拖动isoline时，响应事件
isoLine.sigDragged.connect(updateIsocurve)

# 处理图像项的鼠标悬停事件
## 经过实践对比，该函数实现的功能是：当鼠标移动到图像时，p1绘图区域会显示对应的鼠标位置，图像位置，图像值
def imageHoverEvent(event):
    """Show the position, pixel, and value under the mouse cursor.
    """
    if event.isExit(): # 检查鼠标是否离开了图像项的区域
        p1.setTitle("") # 如果离开了那么显示“’，即不显示内容
        return
    pos = event.pos() # 获取图像项中的鼠标位置
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
img.hoverEvent = imageHoverEvent # 将悬停事件hoverEvent 替换为上述代码
''' 
img.hoverEvent = imageHoverEvent 这行代码将 img 的 hoverEvent 方法替换为我们的自定义 imageHoverEvent 
函数。这是一种“猴子补丁”（monkey-patching）技术，通常不推荐使用，
因为它会改变原有类的行为。正确的方法是子类化 ImageItem 并覆盖 hoverEvent 方法。
但是，对于这种简单的用途，猴子补丁是可以接受的。
''' 

if __name__ == '__main__':
    pg.exec()
