from PIL import Image
import math

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.pixel_data = []
        self.process_image()
        self.map_values()

    def process_image(self):
        try:
            img = Image.open(self.image_path)
            # 获取图像的红色通道数据
            red_channel = img.split()[0]
            width, height = img.size

            # 将红色通道像素值存储为二维列表
            for y in range(height):
                row = []
                for x in range(width):
                    pixel_value = red_channel.getpixel((x, y))
                    row.append(pixel_value)
                self.pixel_data.append(row)

            img.close()

        except Exception as e:
            print(f"发生错误: {e}")
    def map_values(self):
        # 将r值从0-255映射到4-0的范围
        for row in self.pixel_data:
            for i in range(len(row)):
                row[i] = math.ceil(4 - (row[i] / 255.0)*4)

    def print_image(self):
        # 将映射后的值转换为相应的字符，并打印出表示图像的字符串
        for row in self.pixel_data:
            print("".join(["██" if val == 4 else "▓▓" if val == 3 else "▒▒" if val == 2 else "░░"if val == 1 else "　" for val in row]))
