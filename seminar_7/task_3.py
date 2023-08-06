# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

from typing import TextIO


def read_line(file: TextIO) -> str:
    text = file.readline()
    if text == '':
        file.seek(0)
        text = file.readline()
    return text[:-1]


def read_file():
    with (
        open('numbers.txt', encoding="utf-8") as numbers,
        open('names.txt', encoding="utf-8") as names,
        open('result.txt', 'w', encoding="utf-8") as res
    ):
        len_numbers = len(numbers.readlines())
        len_names = len(names.readlines())
        for _ in range(max(len_numbers, len_names)):
            crnt_name = read_line(names)
            crnt_numbers = read_line(numbers)
            a, b = crnt_numbers.split('|')
            mult = int(a) * float(b)
            if mult > 0:
                res.write((crnt_name.upper() + "|" + str(round(mult))) + '\n')
            else:
                res.write((crnt_name.lower() + "|" + str(-mult)) + '\n')


read_file()
