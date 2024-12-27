from ..Rectangle.Rectangle import Rectangle
from ..color.Color import Color

class Square(Rectangle):
    def __init__(self, size, r, g, b):
        self.width = size
        self.height = size
        self.color = Color(r,g,b)
        self.name = "квадрат"
    def repr(self):
        print(f"Длина {self.name}а: {self.width}")
        print(f"Площадь {self.name}а: {self.area()}")
        print(f"Цвет {self.name}а: R: {self.color.r} B: {self.color.b} G: {self.color.g}")
