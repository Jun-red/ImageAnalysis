''' 
    1. 对比度拉伸
    2. https://blog.csdn.net/saltriver/article/details/79677199l
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 参数0  表示以灰度模式读取图像
farina = cv2.imread(r"C:\Users\12284\Desktop\GitHub\ImageAnalysis\images\duibidu.png", 0)

# cv2.calcHist(images, channels, mask, histSize, ranges)
# images 
# channels ：表示从哪些通道计算直方图。在demo中[0]表示只计算第一个通道(灰度图像只有一个通道)的直方图
# None  表示没有掩码
# histSize 表示直方图的尺寸。在demo中 [256]表示直方图将有256个条目，对应灰度级别的值为[0,255]
# ranges 表示直方图中每个条目的范围.在该例中,【0，256】表示直方图的条目将覆盖从0到255的灰度值
## 针对ranges 应该是对应图像中具体的像素值的最小与最大区间
hist_full = cv2.calcHist([farina], [0], None, [256], [0,256])

plt.plot(hist_full)
plt.show()

Imax = np.max(farina)
Imin = np.min(farina)
print("Imax = ", Imax) # 使用numpy的max函数查找farina图像中的最大像素值，这个值将被用作对比度拉伸过程中的原始最大值。
print("Imin = ", Imin) # 这行代码使用NumPy的min函数来找到farina图像中的最小像素值。
Imax = 50
Imin = 20
print(farina)
# 这两个变量定义了拉伸后的目标最大值和最小值。
MAX = 255
MIN = 0
# 这行代码实现了对比度拉伸的公式。
## (farina - Imin) / (Imax - Imin) 将每一个像素值归一化到[0,1]区间
## 将归一化的结果*目标范围MAX-MIN(即255)，然后再加上目标最小值MIN，从而将像素值映射到了目标范围内
farina_cs = (farina - Imin) / (Imax - Imin) * (MAX - MIN) + MIN
# print(farina_cs)
plt.plot(farina_cs)
plt.show()
cv2.imshow("old", farina)
# 将拉伸后的图像farina_cs转换为uint8类型，因为OpenCV期望图像数据是这种类型。
cv2.imshow("new", farina_cs.astype("uint8"))
cv2.waitKey()