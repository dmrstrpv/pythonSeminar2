# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.
import shlex

generator = (n for n in range(0, 101, 2) if (n % 10 + n // 10) != 8)

print(*generator)

# oneliner = map(int(*generator))
s = list(*generator)
s1 = str(s)
print(s)

s = str(input("here"))
s1 = s.split()
s2 = sum(map(int(s1)))
print(s2)


