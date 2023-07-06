# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


input_num = 0
result = 0
num_1 = 0
num_2 = 0
num_3 = 0
SINGLE_DIGIT = 1
SINGLE_DIGIT_END = 9
DOUBLE_DIGIT = 99
TRIPLE_DIGIT = 999
DIGIT_MIN = 1
DIGIT_MAX = 999

while not (1 <= input_num <= 999):
    input_num = int(input("Введите число: "))

if SINGLE_DIGIT < input_num < SINGLE_DIGIT_END:
    result = input_num ** 2
elif SINGLE_DIGIT_END < input_num < DOUBLE_DIGIT:
    result = (input_num % 10) * (input_num // 10)
elif DOUBLE_DIGIT < input_num < TRIPLE_DIGIT:
    num_1 = input_num // 100      # 1
    num_2 = input_num // 10 % 10  # 2
    num_3 = input_num % 10        # 3
    result = num_3 * 100 + num_2 * 10 + num_1

print(result)