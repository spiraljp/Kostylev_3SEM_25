using System;

namespace Lab2_GeometricFigures
{
    public class Square : Rectangle, IPrint
    {
        public Square(double side) : base(side, side)
        {
        }

        public double Side
        {
            get { return Width; }
            set
            {
                if (value <= 0)
                    throw new ArgumentException("Сторона квадрата должна быть положительным числом");

                Width = value;
                Height = value;
            }
        }

        public override string ToString()
        {
            return $"Квадрат: Сторона = {Side:F2}, Площадь = {Area():F2}";
        }
    }
}
