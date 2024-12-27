from tqdm import tqdm
from time import sleep
 
from lab_python_oop.color.Color import Color
from lab_python_oop.circle.Circle import Circle
from lab_python_oop.Rectangle.Rectangle import Rectangle
from lab_python_oop.sqare.Square import Square

N = 32
rect = Rectangle(N, N, 0, 0, 255)
circ = Circle(N, 0, 255, 0)
squ = Square(N, 255, 0, 0)
rect.repr()
circ.repr()
squ.repr()


text = ""
for char in tqdm(["f", "i", "n", "i", "s","h"], ncols=80):
    sleep(1)
    text = text + char
    tqdm.write(text)