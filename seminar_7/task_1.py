# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random as r

_MIN = -1000
_MAX = 1000


def random_nums(lines_num: int, file_name: str):
    with open(file_name, mode="a", encoding="utf-8") as f:
        for _ in range(lines_num):
            n_int: int = r.randint(_MIN, _MAX)
            n_float: float = r.uniform(_MIN, _MAX)
            f.write(str(f'{n_int} | {n_float}' '\n'))


random_nums(8, 'numbers.txt')
