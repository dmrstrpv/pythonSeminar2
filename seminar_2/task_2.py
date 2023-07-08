# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [1, 45, 'text', 2.12, False, 'text']
# index = None
# content = None
# address = None
# item_size = None
# item_hash = None
#
# result: str = ''

for i, item in enumerate(data, start=1):
    address: int = id(item)
    item_size: int = sys.getsizeof(item)
    item_hash: int = hash(item)
    # res_number: bool = isinstance(item, int)
    # res_str: bool = isinstance(item, str)
    if type(item) == int:
        result = ' This ia a number'
    elif isinstance(item, str):
        result = ' This is a string'
    print(f'Номер:{i}, значение: {item}, адрес в памяти: {address},'
          f' размер в памяти: {item_size}, хэш объекта: {item_hash}, {result}')
