# code.py
from operator import itemgetter
from typing import List, Dict, Tuple

class Dirigent:
    """Дирижёр"""
    def __init__(self, id: int, fio: str, salary: int, orchestra_id: int):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.orchestra_id = orchestra_id

class Orchestra:
    """Оркестр"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class DirigentOrchestra:
    """Связь многие-ко-многим между дирижёрами и оркестрами"""
    def __init__(self, dirigent_id: int, orchestra_id: int):
        self.dirigent_id = dirigent_id
        self.orchestra_id = orchestra_id


class OrchestralManager:
    def __init__(self, orchestras: List[Orchestra], dirigents: List[Dirigent],
                 dir_orch: List[DirigentOrchestra]):
        self.orchestras = orchestras
        self.dirigents = dirigents
        self.dir_orch = dir_orch

        # Связи между таблицами
        self.one_to_many = self._create_one_to_many()
        self.many_to_many = self._create_many_to_many()

    def _create_one_to_many(self) -> List[Tuple[str, int, str]]:
        """Создание связи один-ко-многим"""
        return [(d.fio, d.salary, o.name)
                for o in self.orchestras
                for d in self.dirigents
                if d.orchestra_id == o.id]

    def _create_many_to_many(self) -> List[Tuple[str, int, str]]:
        """Создание связи многие-ко-многим"""
        many_to_many_temp = [(o.name, do.orchestra_id, do.dirigent_id)
                            for o in self.orchestras
                            for do in self.dir_orch
                            if o.id == do.orchestra_id]

        return [(d.fio, d.salary, orch_name)
                for orch_name, orch_id, dir_id in many_to_many_temp
                for d in self.dirigents if d.id == dir_id]

    def get_orchestras_starting_with_a(self) -> Dict[str, List[str]]:
        """Задание Г1: Оркестры, начинающиеся на 'А' и их дирижёры"""
        res_1 = {}
        for o in self.orchestras:
            if o.name.startswith('А'):
                o_dirigs = [x for x, _, orch in self.one_to_many if orch == o.name]
                res_1[o.name] = o_dirigs
        return res_1

    def get_max_salary_by_orchestra_sorted(self) -> List[Tuple[str, int]]:
        """Задание Г2: Максимальная зарплата дирижёра в каждом оркестре"""
        res_2 = []
        for o in self.orchestras:
            o_dirigs = list(filter(lambda i: i[2] == o.name, self.one_to_many))
            if o_dirigs:
                max_salary = max([sal for _, sal, _ in o_dirigs])
                res_2.append((o.name, max_salary))
        return sorted(res_2, key=itemgetter(1), reverse=True)

    def get_sorted_many_to_many(self) -> List[Tuple[str, int, str]]:
        """Задание Г3: Сортировка связи многие-ко-многим"""
        return sorted(self.many_to_many, key=itemgetter(2))


# Инициализация данных
def create_test_data():
    orchestras = [
        Orchestra(1, 'Академический оркестр Москвы'),
        Orchestra(2, 'Балтийский оркестр'),
        Orchestra(3, 'Альфа-оркестр Санкт-Петербурга'),
        Orchestra(4, 'Оркестр камерной музыки'),
    ]

    dirigents = [
        Dirigent(1, 'Артамонов', 85000, 1),
        Dirigent(2, 'Белов', 90000, 2),
        Dirigent(3, 'Андреев', 78000, 3),
        Dirigent(4, 'Иванов', 95000, 1),
        Dirigent(5, 'Кузнецов', 87000, 4),
    ]

    dir_orch = [
        DirigentOrchestra(1, 1),
        DirigentOrchestra(2, 2),
        DirigentOrchestra(3, 3),
        DirigentOrchestra(4, 1),
        DirigentOrchestra(5, 4),
        DirigentOrchestra(2, 4),
    ]

    return orchestras, dirigents, dir_orch


def main():
    orchestras, dirigents, dir_orch = create_test_data()
    manager = OrchestralManager(orchestras, dirigents, dir_orch)

    print("Задание Г1")
    res_1 = manager.get_orchestras_starting_with_a()
    print(res_1)

    print("\nЗадание Г2")
    res_2 = manager.get_max_salary_by_orchestra_sorted()
    print(res_2)

    print("\nЗадание Г3")
    res_3 = manager.get_sorted_many_to_many()
    print(res_3)


if __name__ == "__main__":
    main()
