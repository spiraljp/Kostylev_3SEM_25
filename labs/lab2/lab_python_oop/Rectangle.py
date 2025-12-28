from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import Color

class Rectangle(GeometricFigure):
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.colorObj = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {0}, ширина: {1}, высота: {2}, цвет: {3}, площадь: {4}".format(
            self.getName(), self.width, self.height, self.colorObj, self.area())
