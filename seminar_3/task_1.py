# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 33, 33, 43, 43]

# Вариант 1

result = set()
for element in data:
    counter = data.count(element)
    if counter > 0:
        result.add(element)

print(1, list(result))

# Вариант 2

new_data_lst = []
for each in data:
    if each not in new_data_lst:
        new_data_lst.append(each)

print(2, new_data_lst)

# Вариант 3

result = list(set(data))
print(3, result)

