# 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.

import random as r

_QUEENS_NUM: int = 8
_BOARD_SIZE: int = 8

__all__ = ['queen_check_mod']


def queen_check_mod(pos: list[tuple]) -> bool:
    result = True

    for i in range(_QUEENS_NUM):
        if not result:
            break
        row_1, col_1 = pos[i]
        for j in range(i + 1, _QUEENS_NUM):
            row_2, col_2 = pos[j]
            if row_1 == row_2 or col_2 == col_1 or abs(row_1 - row_2) == abs(col_1 - col_2):
                result = False
                break
    return result


def positions() -> list[tuple[int, int]]:
    result = []

    for i in range(_BOARD_SIZE):
        result.append((i, r.randint(1, _BOARD_SIZE)))
    return result


queens = positions()
print(queen_check_mod(queens))

