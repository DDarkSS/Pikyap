from math import pi
from ..Shape.Shape import Shape
from ..color.Color import Color

class Circle(Shape):
    def __init__(self, radius, r, g, b):
        self.radius = radius
        self.color = Color(r, g, b)
        self.name = "круг"
    def area(self):
        return self.radius ** 2 * pi
    def repr(self):
        print(f"Радиус {self.name}а: {self.radius}")
        print(f"Площадь {self.name}а: {self.area()}")
        print(f"Цвет {self.name}а: R: {self.color.r} B: {self.color.b} G: {self.color.g}")
