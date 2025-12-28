using System;

namespace Lab2_GeometricFigures
{
    public abstract class GeometricFigure
    {
        public abstract double Area();

        public override string ToString()
        {
            return $"Фигура: {GetType().Name}, Площадь: {Area():F2}";
        }
    }
}
