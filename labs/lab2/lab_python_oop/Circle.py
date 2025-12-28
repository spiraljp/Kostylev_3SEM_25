import math
from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import Color

class Circle(GeometricFigure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.colorObj = Color(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Фигура: {0}, радиус: {1}, цвет: {2}, площадь: {3:.2f}".format(
            self.getName(), self.radius, self.colorObj, self.area())
