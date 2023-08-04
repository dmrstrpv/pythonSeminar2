# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


from sys import argv
from random import randint as rnd

__all__ = ['pin_code']

START = 0
STOP = 100
ATTEMPTS = 3


def pin_code(start: int, stop: int, attempts: int = ATTEMPTS):
    n = rnd(start, stop)
    cnt = attempts
    flag = False
    while cnt > 0:
        n_usr = int(input('Enter your number: '))
        if n_usr == n:
            print('Success')
            flag = True
        elif n_usr < n:
            print('Greater')
            cnt -= 1
        else:
            print('Smaller')
            cnt -= 1
    return flag


if __name__ == '__main__':
    name, *param = argv
    print(pin_code(*(int(n) for n in param)))

