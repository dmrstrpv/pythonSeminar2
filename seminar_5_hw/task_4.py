# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

from collections.abc import Generator

def fibonacci_gen(n: int) -> Generator[int]:
    n1, n2 = 0, 1
    if n > 1:
        for _ in range(n):
            yield n1
            n1, n2 = n2, n1 + n2


print(*fibonacci_gen(int(input("Enter your number: "))))

