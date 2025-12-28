using System;
using System.Globalization;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("=== Решение биквадратного уравнения ===");
        Console.WriteLine("Уравнение вида: Ax^4 + Bx^2 + C = 0");

        double a, b, c;

        // Обработка аргументов командной строки
        if (args.Length >= 3)
        {
            if (TryParseCoefficient(args[0], out a) &&
                TryParseCoefficient(args[1], out b) &&
                TryParseCoefficient(args[2], out c))
            {
                Console.WriteLine($"Коэффициенты из командной строки: A={a}, B={b}, C={c}");
                SolveBiquadraticEquation(a, b, c);
                return;
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Ошибка: неверные коэффициенты в аргументах командной строки");
                Console.ResetColor();
            }
        }

        // Ввод с клавиатуры
        a = ReadCoefficient("A");
        b = ReadCoefficient("B");
        c = ReadCoefficient("C");

        SolveBiquadraticEquation(a, b, c);
    }

    static double ReadCoefficient(string coefficientName)
    {
        while (true)
        {
            Console.Write($"Введите коэффициент {coefficientName}: ");
            string input = Console.ReadLine();

            if (double.TryParse(input, NumberStyles.Any, CultureInfo.InvariantCulture, out double value))
            {
                return value;
            }

            Console.WriteLine($"Ошибка: '{input}' не является числом. Попробуйте снова.");
        }
    }

    static bool TryParseCoefficient(string input, out double value)
    {
        return double.TryParse(input, NumberStyles.Any, CultureInfo.InvariantCulture, out value);
    }

    static void SolveBiquadraticEquation(double a, double b, double c)
    {
        if (a == 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения");
            Console.ResetColor();
            return;
        }

        // Решаем квадратное уравнение относительно t = x^2
        double discriminant = b * b - 4 * a * c;

        Console.WriteLine($"\nДискриминант D = {discriminant:F2}");

        if (discriminant < 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Действительных корней нет");
            Console.ResetColor();
            return;
        }

        if (discriminant == 0)
        {
            double t = -b / (2 * a);

            Console.ForegroundColor = ConsoleColor.Green;
            if (t > 0)
            {
                double x1 = Math.Sqrt(t);
                double x2 = -Math.Sqrt(t);
                Console.WriteLine($"Два корня: x1 = {x1:F4}, x2 = {x2:F4}");
            }
            else if (t == 0)
            {
                Console.WriteLine($"Один корень: x = 0");
            }
            else
            {
                Console.WriteLine($"Действительных корней нет (t = {t:F4} < 0)");
            }
            Console.ResetColor();
            return;
        }

        // discriminant > 0
        double sqrtD = Math.Sqrt(discriminant);
        double t1 = (-b + sqrtD) / (2 * a);
        double t2 = (-b - sqrtD) / (2 * a);

        Console.ForegroundColor = ConsoleColor.Green;
        int rootCount = 0;

        if (t1 > 0)
        {
            double x1 = Math.Sqrt(t1);
            double x2 = -Math.Sqrt(t1);
            Console.WriteLine($"Корни из t1: x1 = {x1:F4}, x2 = {x2:F4}");
            rootCount += 2;
        }
        else if (t1 == 0)
        {
            Console.WriteLine($"Корень из t1: x = 0");
            rootCount += 1;
        }

        if (t2 > 0)
        {
            double x3 = Math.Sqrt(t2);
            double x4 = -Math.Sqrt(t2);
            Console.WriteLine($"Корни из t2: x3 = {x3:F4}, x4 = {x4:F4}");
            rootCount += 2;
        }
        else if (t2 == 0)
        {
            Console.WriteLine($"Корень из t2: x = 0");
            rootCount += 1;
        }

        if (rootCount == 0)
        {
            Console.ResetColor();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Действительных корней нет");
        }
        else
        {
            Console.WriteLine($"Всего действительных корней: {rootCount}");
        }

        Console.ResetColor();
    }
}
