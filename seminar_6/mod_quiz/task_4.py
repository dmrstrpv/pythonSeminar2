# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


START = 0
STOP = 100
ATTEMPTS = 3


def quiz_game(s: str, answers: str, attempts: int = ATTEMPTS):
    print(s)
    cnt = attempts
    while cnt > 0:
        current_try = input(f'Attempts left: {cnt}. Your answer: ')
        if current_try in answers:
            return cnt
        cnt -= 1
    else:
        return attempts


if __name__ == '__main__':

    print(quiz_game('Puzzle', ['yes', 'no']))

