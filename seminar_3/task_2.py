# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


some_text = input("Введите данные: ")

if some_text.count("-") == 0 and some_text.isdecimal():
    result = int(some_text)
elif some_text.count("-") <= 1 and some_text[1:].count('-') == 0 and \
        some_text.replace(".", "", 1).replace('-', '', 1).isdecimal():
    result = float(some_text)
elif not some_text.islower():
    result = some_text.lower()
else:
    result = some_text.upper()

print(result, type(result))
