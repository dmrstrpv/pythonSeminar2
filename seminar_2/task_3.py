# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BINARY_DIVISOR = 2
OCT_DIVISOR = 8


def get_number_from_user() -> tuple[int, int]:
    info = input("Please enter a number and a divisor: ")
    r, d = info.split()
    return int(r), int(d)


def converter(dividend: int, divisor: int):
    r: str = ''
    while dividend > 0:
        r = str(dividend % divisor) + r
        dividend //= divisor
    return r


dividend, divisor = get_number_from_user()
if isinstance(dividend, int) and divisor in (BINARY_DIVISOR, OCT_DIVISOR):
    print(converter(dividend, divisor))
else:
    print("Wrong number. Try again!")


