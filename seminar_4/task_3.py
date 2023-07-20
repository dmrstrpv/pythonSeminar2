# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def get_dict_unicode_chars(str_nums : str) -> dict[str: int]:
    num1, num2 = map(int, str_nums.split())
    unicode_dict = {}
    for i in round(min(num1, num2), max(num1, num2) + 1):
        unicode_dict[chr(i)] = i
    return unicode_dict


input_str = input("Введите: ")

get_dict_unicode_chars(input_str)

