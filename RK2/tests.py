# tests.py
import unittest
from code import Orchestra, Dirigent, DirigentOrchestra, OrchestralManager, create_test_data


class TestOrchestralManager(unittest.TestCase):
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.orchestras, self.dirigents, self.dir_orch = create_test_data()
        self.manager = OrchestralManager(self.orchestras, self.dirigents, self.dir_orch)

    def test_get_orchestras_starting_with_a(self):
        """Тест для задания Г1: оркестры на 'А'"""
        print("\nЗапуск теста Г1: Оркестры на 'А' и их дирижёры")

        result = self.manager.get_orchestras_starting_with_a()

        # Проверяем, что результат - словарь
        self.assertIsInstance(result, dict)

        # Проверяем, что есть только оркестры на 'А'
        for orchestra_name in result.keys():
            self.assertTrue(orchestra_name.startswith('А'))

        # Проверяем конкретные оркестры
        expected_orchestras = ['Академический оркестр Москвы', 'Альфа-оркестр Санкт-Петербурга']
        self.assertEqual(set(result.keys()), set(expected_orchestras))

        # Проверяем дирижёров для академического оркестра
        akadem_dirs = result['Академический оркестр Москвы']
        self.assertEqual(len(akadem_dirs), 2)
        self.assertIn('Артамонов', akadem_dirs)
        self.assertIn('Иванов', akadem_dirs)

        print("✅ Тест Г1 пройден: найдены оркестры на 'А' с их дирижёрами")

    def test_get_max_salary_by_orchestra_sorted(self):
        """Тест для задания Г2: максимальная зарплата по оркестрам"""
        print("\nЗапуск теста Г2: Максимальная зарплата по оркестрам")

        result = self.manager.get_max_salary_by_orchestra_sorted()

        # Проверяем, что результат - список кортежей
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) and len(item) == 2 for item in result))

        # Проверяем сортировку по убыванию зарплаты
        salaries = [salary for _, salary in result]
        self.assertEqual(salaries, sorted(salaries, reverse=True))

        # Проверяем конкретные значения
        expected_data = [
            ('Академический оркестр Москвы', 95000),
            ('Оркестр камерной музыки', 90000),  # Белов (90000) > Кузнецов (87000)
            ('Балтийский оркестр', 90000),
            ('Альфа-оркестр Санкт-Петербурга', 78000),
        ]

        for i, (orch_name, salary) in enumerate(result):
            self.assertEqual(orch_name, expected_data[i][0])
            self.assertEqual(salary, expected_data[i][1])

        print("✅ Тест Г2 пройден: максимальные зарплаты отсортированы правильно")

    def test_get_sorted_many_to_many(self):
        """Тест для задания Г3: сортировка связи многие-ко-многим"""
        print("\nЗапуск теста Г3: Сортировка связи многие-ко-многим")

        result = self.manager.get_sorted_many_to_many()

        # Проверяем, что результат отсортирован по названию оркестра (3-й элемент кортежа)
        orch_names = [orch_name for _, _, orch_name in result]
        self.assertEqual(orch_names, sorted(orch_names))

        # Проверяем структуру данных
        for item in result:
            self.assertEqual(len(item), 3)  # (ФИО, зарплата, оркестр)
            self.assertIsInstance(item[0], str)  # ФИО
            self.assertIsInstance(item[1], int)  # зарплата
            self.assertIsInstance(item[2], str)  # оркестр

        # Проверяем первое значение (самое первое по алфавиту)
        self.assertEqual(result[0][2], 'Академический оркестр Москвы')

        print("✅ Тест Г3 пройден: связь многие-ко-многим отсортирована по оркестрам")


if __name__ == "__main__":
    # Запуск тестов с подробным выводом
    print("=" * 60)
    print("ЗАПУСК МОДУЛЬНЫХ ТЕСТОВ")
    print("=" * 60)
    unittest.main(verbosity=2)
