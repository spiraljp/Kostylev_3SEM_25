from operator import itemgetter

#Вариант Г 17
class Dirigent:
    """Дирижёр"""
    def __init__(self, id, fio, salary, orchestra_id):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.orchestra_id = orchestra_id

class Orchestra:
    """Оркестр"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DirigentOrchestra:
    """Связь многие-ко-многим между дирижёрами и оркестрами"""
    def __init__(self, dirigent_id, orchestra_id):
        self.dirigent_id = dirigent_id
        self.orchestra_id = orchestra_id



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


def main():

    one_to_many = [(d.fio, d.salary, o.name)
                   for o in orchestras
                   for d in dirigents
                   if d.orchestra_id == o.id]

    many_to_many_temp = [(o.name, do.orchestra_id, do.dirigent_id)
                         for o in orchestras
                         for do in dir_orch
                         if o.id == do.orchestra_id]

    many_to_many = [(d.fio, d.salary, orch_name)
                    for orch_name, orch_id, dir_id in many_to_many_temp
                    for d in dirigents if d.id == dir_id]


    print("Задание Г1")
    res_1 = {}
    for o in orchestras:
        if o.name.startswith('А'):
            o_dirigs = [x for x, _, orch in one_to_many if orch == o.name]
            res_1[o.name] = o_dirigs
    print(res_1)


    print("\nЗадание Г2")
    res_2 = []
    for o in orchestras:
        o_dirigs = list(filter(lambda i: i[2] == o.name, one_to_many))
        if o_dirigs:
            max_salary = max([sal for _, sal, _ in o_dirigs])
            res_2.append((o.name, max_salary))
    res_2_sorted = sorted(res_2, key=itemgetter(1), reverse=True)
    print(res_2_sorted)


    print("\nЗадание Г3")
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == "__main__":
    main()
