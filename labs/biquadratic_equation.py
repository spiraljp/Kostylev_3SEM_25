"""
Программа для решения биквадратного уравнения вида: Ax^4 + Bx^2 + C = 0
"""

import sys
import math

def get_valid_coefficient(prompt, value=None):

    if value is not None:
        try:
            coefficient = float(value)
            print(f"Коэффициент из командной строки: {coefficient}")
            return coefficient
        except ValueError:
            print(f"Некорректное значение коэффициента из командной строки: '{value}'. Требуется ввод с клавиатуры.")

    while True:
        try:
            user_input = input(prompt)
            coefficient = float(user_input)
            return coefficient
        except ValueError:
            print("Ошибка! Введите действительное число.")

def solve_biquadratic(a, b, c):

    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение 0 = 0 имеет бесконечно много решений")
                return ["Любое действительное число"]
            else:
                print(f"Уравнение {c} = 0 не имеет решений")
                return []
        else:
            print(f"Уравнение становится квадратным: {b}x^2 + ({c}) = 0")
            return solve_quadratic_for_t(b, c, a)

    print(f"\nРешаем биквадратное уравнение: ", end="")
    terms = []
    if a != 0:
        terms.append(f"{a}x⁴")
    if b != 0:
        sign = "+" if b > 0 else ""
        terms.append(f"{sign}{b}x²")
    if c != 0:
        sign = "+" if c > 0 else ""
        terms.append(f"{sign}{c}")
    print(" ".join(terms) + " = 0")

    D = b**2 - 4*a*c

    print(f"Дискриминант D = B² - 4AC = {b}² - 4*{a}*{c} = {D}")

    if D < 0:
        print("D < 0: Уравнение не имеет действительных корней")
        return []

    sqrt_D = math.sqrt(D)
    t1 = (-b + sqrt_D) / (2*a)
    t2 = (-b - sqrt_D) / (2*a)

    print(f"Корни для t = x²:")
    print(f"  t₁ = (-B + √D) / (2A) = ({-b} + {sqrt_D:.3f}) / ({2*a}) = {t1:.3f}")
    print(f"  t₂ = (-B - √D) / (2A) = ({-b} - {sqrt_D:.3f}) / ({2*a}) = {t2:.3f}")


    real_roots = []


    if t1 > 0:
        x1 = math.sqrt(t1)
        x2 = -math.sqrt(t1)
        real_roots.extend([x1, x2])
        print(f"t₁ = {t1:.3f} > 0, дает два корня: x₁ = {x1:.3f}, x₂ = {x2:.3f}")
    elif t1 == 0:
        x = 0.0
        real_roots.append(x)
        print(f"t₁ = {t1:.3f} = 0, дает один корень: x = {x:.3f}")
    else:
        print(f"t₁ = {t1:.3f} < 0, не дает действительных корней")

    if t2 != t1:
        if t2 > 0:
            x3 = math.sqrt(t2)
            x4 = -math.sqrt(t2)
            if not any(math.isclose(x3, root, rel_tol=1e-9) for root in real_roots):
                real_roots.extend([x3, x4])
                print(f"t₂ = {t2:.3f} > 0, дает два корня: x₃ = {x3:.3f}, x₄ = {x4:.3f}")
        elif t2 == 0 and 0 not in real_roots:
            x = 0.0
            real_roots.append(x)
            print(f"t₂ = {t2:.3f} = 0, дает один корень: x = {x:.3f}")
        elif t2 < 0:
            print(f"t₂ = {t2:.3f} < 0, не дает действительных корней")

    return sorted(real_roots)

def solve_quadratic_for_t(b, c, a):

    print(f"\nРешаем квадратное уравнение: {b}x² + ({c}) = 0")

    if b == 0:
        if c == 0:
            print("Уравнение 0 = 0 имеет бесконечно много решений")
            return ["Любое действительное число"]
        else:
            print(f"Уравнение {c} = 0 не имеет решений")
            return []


    if -c/b < 0:
        print(f"x² = {-c}/{b} = {-c/b:.3f} < 0, уравнение не имеет действительных корней")
        return []

    x_squared = -c/b
    if x_squared == 0:
        x = 0.0
        print(f"x² = {x_squared}, уравнение имеет один корень: x = {x:.3f}")
        return [x]

    x1 = math.sqrt(x_squared)
    x2 = -x1
    print(f"x² = {-c}/{b} = {x_squared:.3f}, уравнение имеет два корня: x₁ = {x1:.3f}, x₂ = {x2:.3f}")
    return sorted([x1, x2])

def main():
    """Основная функция программы"""
    print("=" * 60)
    print("РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ: Ax⁴ + Bx² + C = 0")
    print("=" * 60)

    coefficients_from_cli = [None, None, None]


    if len(sys.argv) > 1:
        coefficients_from_cli[0] = sys.argv[1] if len(sys.argv) > 1 else None
    if len(sys.argv) > 2:
        coefficients_from_cli[1] = sys.argv[2] if len(sys.argv) > 2 else None
    if len(sys.argv) > 3:
        coefficients_from_cli[2] = sys.argv[3] if len(sys.argv) > 3 else None

    print("\nВведите коэффициенты биквадратного уравнения Ax⁴ + Bx² + C = 0")
    print("(Коэффициенты можно задать как параметры командной строки)")

    a = get_valid_coefficient("Введите коэффициент A: ", coefficients_from_cli[0])
    b = get_valid_coefficient("Введите коэффициент B: ", coefficients_from_cli[1])
    c = get_valid_coefficient("Введите коэффициент C: ", coefficients_from_cli[2])

    roots = solve_biquadratic(a, b, c)


    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 60)

    if not roots:
        print("Уравнение не имеет действительных корней")
    elif roots == ["Любое действительное число"]:
        print("Уравнение имеет бесконечно много решений:")
        print("  x ∈ ℝ (любое действительное число)")
    else:
        if len(roots) == 1:
            print(f"Уравнение имеет 1 действительный корень:")
            print(f"  x = {roots[0]:.6f}")
        else:
            print(f"Уравнение имеет {len(roots)} действительных корня:")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root:.6f}")

    print("\nПроверка корней:")
    for root in roots:
        if root != "Любое действительное число":
            result = a * root**4 + b * root**2 + c
            print(f"  Для x = {root:.6f}: A·x⁴ + B·x² + C = {result:.10f} ≈ 0")

if __name__ == "__main__":
    main()
