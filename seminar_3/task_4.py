# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

from collections import defaultdict


DUPLICATES = 2

data = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 33, 43, 43]
my_dict = defaultdict(int)

for element in data:
    my_dict[element] += 1

for key, value in my_dict.items():
    if value == DUPLICATES:
        for _ in range(DUPLICATES):
            data.remove(key)

print(dict(my_dict))
print(data)


# DUPLICATES = 3
#
# data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 33, 33, 43, 43]
# my_dict = {}
#
# for element in data:
#     value = my_dict.setdefault(element, 0)
#     my_dict[element] += 1
#
# for key, value in my_dict.items():
#     if value == DUPLICATES:
#         for _ in range(DUPLICATES):
#             data.remove(key)
#
# print(data)

