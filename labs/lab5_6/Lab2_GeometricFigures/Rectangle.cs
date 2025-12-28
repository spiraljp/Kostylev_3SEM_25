using System;

namespace Lab2_GeometricFigures
{
    public class Rectangle : GeometricFigure, IPrint
    {
        public double Width { get; set; }
        public double Height { get; set; }

        public Rectangle(double width, double height)
        {
            if (width <= 0 || height <= 0)
                throw new ArgumentException("Ширина и высота должны быть положительными числами");

            Width = width;
            Height = height;
        }

        public override double Area()
        {
            return Width * Height;
        }

        public override string ToString()
        {
            return $"Прямоугольник: Ширина = {Width:F2}, Высота = {Height:F2}, Площадь = {Area():F2}";
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
