# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [1, 5, 1, 43, 2, 2, 3, 3, 4, 33, 6, 4, 5, 5, 33, 8, 8, 8, 6, 6, 7, 7]

print(1, data)


def copy_double_lst(array: list[int]) -> list[int]:
    result = set()
    for each in array:
        count = array.count(each)
        if count > 0:
            result.add(each)
    return list(result)


print(2, copy_double_lst(data))


# Variant 2
print(f'Вариант 2 -> 1 {data}')
print(f'Вариант 2 -> 2 {list(set(data))}')

