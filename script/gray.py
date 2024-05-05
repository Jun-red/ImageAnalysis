from PIL import Image

# 打开图像文件
image = Image.open("images/user_profile_bak.png")

# 转换为灰度图像
gray_image = image.convert("L")
gray_image.save("test.png")
# 获取图像的宽度和高度
# width, height = gray_image.size

# # 遍历图像的每个像素
# for x in range(width):
#     for y in range(height):
#         # 获取像素点的 RGB 值
#         r, g, b = gray_image.getpixel((x, y))
#         # 如果不是白色，将像素设置为灰色
#         if (r, g, b) != (255, 255, 255):
#             gray_image.putpixel((x, y), (128, 128, 128))

# # 保存处理后的图像
# gray_image.save("processed_image.png")
