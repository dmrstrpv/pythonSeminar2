# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def random_names():
    vowel_list = 'аааауууууееееииииооооууыэюя'
    consonants_list = 'бвгджзклмнпртсфчхшщ'

    def gen_name(code):
        return "".join(random.choice(vowel_list if c == '0' else consonants_list) for c in code)

    codes = ['0', '1', '01', '10', '010', '101']
    types = [gen_name(code) for code in codes]

    return ''.join(random.sample(types, 3))


def validate_names():
    while True:
        name = random_names()
        if 4 < len(name) < 7:
            break
    return name


def write_file(lines_num=5, file_name='names.txt'):
    with open(file_name, mode="a", encoding="utf-8") as f:
        for _ in range(lines_num + 1):
            f.write(validate_names().capitalize() + '\n')


write_file()
