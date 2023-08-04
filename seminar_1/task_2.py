# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


year = int(input("Введите год: "))
GREGORIAN_YEAR = 1583

IS_LEAP = "{} високосный год"
IS_NOT_LEAP = "{} не високосный год"
IS_NOT_GREGORIAN_YEAR = "{} год не в Григорианском календаре"
DIVISOR_4 = 4
DIVISOR_100 = 100
DIVISOR_400 = 400
result = ""

if year <= GREGORIAN_YEAR:
    result = IS_NOT_GREGORIAN_YEAR.format(year)
elif year % DIVISOR_100 != 0 and year % DIVISOR_4 == 0 or year % DIVISOR_400 == 0:
    result = IS_LEAP.format(year)
else:
    result = IS_NOT_LEAP.format(year)

print(result)
