using System;

namespace Lab2_GeometricFigures
{
    public class Circle : GeometricFigure, IPrint
    {
        public double Radius { get; set; }

        public Circle(double radius)
        {
            if (radius <= 0)
                throw new ArgumentException("Радиус должен быть положительным числом");

            Radius = radius;
        }

        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }

        public override string ToString()
        {
            return $"Круг: Радиус = {Radius:F2}, Площадь = {Area():F2}";
        }

        public void Print()
        {
            Console.WriteLine(ToString());
        }
    }
}
