# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


data = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 33, 43, 43]
new_data_lst = []

print(data)

for element in range(len(data)):
    if data[element] % 2 != 0:
        new_data_lst.append(element + 1)

print(new_data_lst)


data1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 33, 43, 43]
new_data_lst1 = []

for i, value in enumerate(data1, start=1):
    if value % 2 == 1:
        new_data_lst1.append(i)

print(new_data_lst1)

