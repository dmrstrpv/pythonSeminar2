# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as rnd

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
    data = input('Enter: ')
    start, stop = map(int, data.split())
    pin_code(start, stop)
