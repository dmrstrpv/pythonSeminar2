# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».

n = int(input("Enter your number: "))


def foo_my_gen(n: int):
    cnt: int = 2
    while 1 < cnt <= n:
        is_prime: bool = True
        for i in range(2, cnt//2 + 1):
            if cnt%i == 0:
                cnt += 1
                is_prime = False
                break
        if is_prime:
            yield cnt
            cnt += 1


for n in (foo_my_gen(n)):
    print(n, end=' ')



