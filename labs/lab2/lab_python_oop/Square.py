from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "Фигура: {0}, сторона: {1}, цвет: {2}, площадь: {3}".format(
            self.getName(), self.width, self.colorObj, self.area())
