# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random as r
from string import ascii_lowercase, digits


def file_maker(extn: str, _min_name_len: int = 6, _max_name_len: int = 30,
               _min_byte_len: int = 256, _max_byte_len: int = 4096, quantity: int = 10) -> None:
    for i in range(quantity):
        name = ''.join(r.choices(ascii_lowercase + digits + "_", k=r.randint(_min_name_len, _max_name_len)))
        _bytes = bytes(r.randint(0, 255) for _ in range(_min_byte_len, _max_byte_len))
        with open(rf"sem_7_tsk_4\{name}.{extn}", 'wb') as files:
            files.write(_bytes)


file_maker("txt")


def extensions(**kwargs):
    for ext, quant in kwargs.items():
        file_maker(ext, quantity=quant)


extensions(txt=3, jpeg=5, png=5)
