# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


num = int(input("Введите число: "))
hex_numbers = "0123456789ABCDEF"


def hex_converter(number):
    number_hex = ""
    while number != 0:
        number_hex = hex_numbers[number % 16] + number_hex
        number //= 16
        if number == 0:
            return number_hex


print(hex_converter(num))


print(hex(int(input("Проверим: ")))[2:].upper())

