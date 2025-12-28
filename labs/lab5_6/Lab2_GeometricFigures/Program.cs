using System;
using System.Collections.Generic;

namespace Lab2_GeometricFigures
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Лабораторная работа №2: Геометрические фигуры ===\n");

            // Создаем коллекцию фигур
            List<GeometricFigure> figures = new List<GeometricFigure>();

            // Добавляем различные фигуры
            figures.Add(new Rectangle(5, 3));
            figures.Add(new Square(4));
            figures.Add(new Circle(2.5));
            figures.Add(new Rectangle(7.2, 4.1));
            figures.Add(new Square(6));
            figures.Add(new Circle(3));

            // Выводим информацию о фигурах
            Console.WriteLine("Список фигур:");
            Console.WriteLine(new string('-', 50));

            foreach (var figure in figures)
            {
                // Используем интерфейс IPrint, если фигура его реализует
                if (figure is IPrint printable)
                {
                    printable.Print();
                }
                else
                {
                    Console.WriteLine(figure);
                }
            }

            Console.WriteLine(new string('-', 50));

            // Сравнение площадей
            Console.WriteLine("\nСравнение площадей:");
            if (figures.Count >= 2)
            {
                Console.WriteLine($"Площадь первой фигуры ({figures[0]}) = {figures[0].Area():F2}");
                Console.WriteLine($"Площадь второй фигуры ({figures[1]}) = {figures[1].Area():F2}");

                if (figures[0].Area() > figures[1].Area())
                    Console.WriteLine("Первая фигура имеет большую площадь");
                else if (figures[0].Area() < figures[1].Area())
                    Console.WriteLine("Вторая фигура имеет большую площадь");
                else
                    Console.WriteLine("Фигуры имеют одинаковую площадь");
            }

            // Демонстрация работы с конкретными типами
            Console.WriteLine("\nДемонстрация работы с конкретными типами:");
            Console.WriteLine(new string('-', 50));

            Rectangle rect = new Rectangle(10, 5);
            Square square = new Square(7);
            Circle circle = new Circle(4);

            rect.Print();
            square.Print();
            circle.Print();

            Console.WriteLine(new string('-', 50));
            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
