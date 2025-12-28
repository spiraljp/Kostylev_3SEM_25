import json
import sys
from field import field
from unique import Unique
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1

# Импортируем все нужные функции
try:
    path = sys.argv[1]
except IndexError:
    path = "data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    # Сортированный список профессий без повторений (игнорируя регистр)
    professions = list(field(arg, 'job-name'))
    unique_professions = list(Unique(professions, ignore_case=True))
    return sorted(unique_professions, key=lambda x: x.lower())


@print_result
def f2(arg):
    # Фильтруем только профессии, начинающиеся со слова "программист"
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    # Добавляем "с опытом Python" к каждой профессии
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    # Генерируем зарплаты и объединяем с профессиями
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
