from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

N = 14

def main():
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

    figures = [rectangle, circle, square]
    print("\nВсе фигуры:")
    for figure in figures:
        print(f"  - {figure.getName()}: площадь = {figure.area():.2f}")

    s = [431, 398, 423, 401, 423, 404, 389, 428, 402, 404, 427, 398, 422, 409, 420, 422, 397, 458, 403, 411, 398, 408, 438, 414, 413, 404, 426, 434, 430, 397, 383, 415, 418, 438, 394, 417, 412, 404, 389, 398, 431, 423, 401, 423, 435, 427, 428, 405, 414, 415, 439, 409, 391, 416, 419, 401, 372, 395, 418, 413, 407, 445, 428, 420, 429, 395, 433, 406, 402, 398, 399, 432, 405, 412, 425, 417, 424, 416, 396, 403, 432, 402, 431, 419, 423, 441, 424, 410, 424, 413, 393, 412, 302, 408, 437, 416, 436, 415, 421, 407, 404, 404, 403, 434, 412, 419, 405, 402, 394, 423, 398, 415, 401, 398, 428, 416, 453, 371, 424, 417]
    print(sorted(s))
    print(len(set(s)))

if __name__ == "__main__":
    main()
