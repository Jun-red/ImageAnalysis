"""
Demonstrates some customized mouse interaction by drawing a crosshair that follows 
the mouse.
通过绘制跟随鼠标的十字线来演示一些自定义的鼠标交互。
"""

''' 
代码来源 : 
import pyqtgraph.examples

pyqtgraph.examples.run()

案例：
    Crosshair / Mouse interaction
''' 

import numpy as np

import pyqtgraph as pg

#generate layout
''' 
这行代码创建了一个 QApplication 实例，这是所有 PyQt5 应用的核心对象，
用于管理图形用户界面应用程序的控制流和主要设置。mkQApp 是 pyqtgraph 提供的一个便捷函数，
用于创建 QApplication。参数 “Crosshair Example” 是应用程序的名称。
''' 
app = pg.mkQApp("Crosshair Example")  # Crosshair Example -> 译: 十字线示例
# 创建一个布局实例，他是pyqtgraph中用于布局和显示图形项的一个容器，参数show=true 指定创建的窗口应该立即显示
win = pg.GraphicsLayoutWidget(show=True)
# 设置窗口的标题
win.setWindowTitle('pyqtgraph example: crosshair') 
# 创建一个标签项（LabelItem），用于显示文本； justify='right' 表示文本右对齐
label = pg.LabelItem(justify='right')
# 将创建的标签项添加到图形窗口中
win.addItem(label)
# 在第1行 第0列添加一个绘图区域（PlotItem）
p1 = win.addPlot(row=1, col=0)  # 这里为什么不是 row = 0 ? 因为win.addItem(label) 占用了第0行
# customize the averaged curve that can be activated from the context menu: 自定义可以从上下文菜单激活的平均曲线：
p1.avgPen = pg.mkPen('#FFFFFF') # 平均曲线的颜色
p1.avgShadowPen = pg.mkPen('#8080DD', width=10) # 平均曲线的阴影颜色和宽度
# 在第2行处创建一个新的绘图区域 P2
p2 = win.addPlot(row=2, col=0)

# 创建一个线性区域项，他可以在绘图区域上拖动，用来表示一个数据区域
region = pg.LinearRegionItem()
# 设置Z值缓冲(深度)
region.setZValue(10)
# Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this 
# item when doing auto-range calculations.
# 这行代码将线性区域项添加到 p2 绘图区域中。参数 ignoreBounds=True 指定在计算自动范围时忽略这个区域项。
p2.addItem(region, ignoreBounds=True)

#pg.dbg()
p1.setAutoVisible(y=True) # 设置p1的自动可见性，参数y=false指定在数据范围变化时自动调整y轴的可见范围

# ===============================================================================================
# 总的来说，这段代码设置了一个交互式图表，其中线性区域项和绘图区域 p1 的范围是相互连接的。用户可以通过拖动线性区域项来选择 p1 中的特定区间，并且当 p1 的视图范围改变时，线性区域项也会自动更新以匹配新的范围。这种交互性使得用户能够方便地探索和分析数据。

#create numpy arrays
#make the numbers large to show that the range shows data from 10000 to all the way 0
data1 = 10000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
data2 = 15000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
print(len(data1))
print(type(data1))
p1.plot(data1, pen="r") # 在绘图区域p1中绘制data1数组的数据，使用红色笔
p1.plot(data2, pen="g") # 在绘图区域p1中绘制data2数组的数据，使用g笔

p2d = p2.plot(data1, pen="w") # 在绘图区域p2中绘制data1数组的数据，使用白色笔，并将返回的绘图项引用赋给变量 p2d。
# 将之前创建的线性区域项region绑定到p2d绘图项上，这意味着线性区域项的移动将受到p2d数据范围的限制，确保用户只能选择data1数据范围内的部分进行查看或分析
# bound the LinearRegionItem to the plotted data
region.setClipItem(p2d)

def update():
    region.setZValue(10)
    minX, maxX = region.getRegion() # 获取当前选定区间的最小值和最大值
    # 将p1绘图区域的x轴范围设置为线性区域项定义的最小值和最大值， padding=0表示不添加任何额外的填充控件
    p1.setXRange(minX, maxX, padding=0)    

region.sigRegionChanged.connect(update)

def updateRegion(window, viewRange):
    rgn = viewRange[0]
    print("#####",rgn)
    region.setRegion(rgn)
# 每当 p1 的视图范围发生变化时（例如用户缩放或平移），updateRegion 函数将被调用，从而更新线性区域项的范围。
p1.sigRangeChanged.connect(updateRegion)
# 这行代码初始化线性区域项的范围，将其设置为从 1000 到 2000 的区间。这样，在应用程序启动时，线性区域项就会显示在这个指定的范围内
region.setRegion([1000, 2000])

# ========================================================================================

#cross hair
vLine = pg.InfiniteLine(angle=90, movable=False)
hLine = pg.InfiniteLine(angle=0, movable=False)
p1.addItem(vLine, ignoreBounds=True)
p1.addItem(hLine, ignoreBounds=True)


vb = p1.vb

def mouseMoved(evt):
    pos = evt
    if p1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index > 0 and index < len(data1):
            label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())



p1.scene().sigMouseMoved.connect(mouseMoved)


if __name__ == '__main__':
    pg.exec()
