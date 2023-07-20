# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

nums = [10, 2, 45, 9, 33, 80, 22, 5, 67, 5, 45]


def bubble_sort(num_lst: list[int]) -> list[int]:
    for i in range(len(num_lst) - 1):
        for j in range(i + 1, len(num_lst)):
            if num_lst[j] < num_lst[i]:
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
    return num_lst


print(nums)
print(bubble_sort(nums))
print(nums)


print([0 * 2])
print([0] * 2)
x = [[0] * 2] * 2
x[0][0] = 4
print(x)

print([[0] * 2] * 2)




