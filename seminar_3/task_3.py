# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.


some_tuple = (2, -6.4, 'string', False, 645, None, 345.2, 0.0034, '83', True)
my_dict = {}

for value in some_tuple:
    if type(value) in my_dict.keys():
        my_dict[type(value)].append(value)
    else:
        my_dict[type(value)] = [value]

print(my_dict)
print(some_tuple)

for value in some_tuple:
    key = my_dict.setdefault(type(value), list())
    key.append(value)

print(my_dict)
