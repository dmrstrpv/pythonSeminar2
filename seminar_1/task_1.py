n = int(input("Введите целое число: "))
e = int(input("Введите целое кратности: "))

result_sum = 0
i = n
while i >= 0:
    if i % 2 == 0 and i % e != 0:
        result_sum += i
    i -= 1

print(result_sum)
