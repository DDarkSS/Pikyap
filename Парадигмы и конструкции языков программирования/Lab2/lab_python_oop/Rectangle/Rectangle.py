from ..Shape.Shape import Shape
from ..color.Color import Color

class Rectangle(Shape):
    def __init__(self, width, height, r, g, b):
        self.width = width
        self.height = height
        self.color = Color(r, g, b)
        self.name = "прямоугольник"
    def area(self):
        return self.width * self.height
    def get_name(self):
        return self.name
    def repr(self):
        print(f"Длина {self.name}а: {self.width}")
        print(f"Ширина {self.name}а: {self.height}")
        print(f"Площадь {self.name}а: {self.area()}")
        print(f"Цвет {self.name}а: R: {self.color.r} B: {self.color.b} G: {self.color.g}")
