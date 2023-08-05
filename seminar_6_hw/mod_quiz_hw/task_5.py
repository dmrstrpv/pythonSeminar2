# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


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


def quiz_dict(attempts: int = 3):
    q_dict = {
        'puzzle': ['yes', 'no'],
        'next puzzle': ['yes', 'no'],
        'yeah': ['yes', 'no']
    }

    for s, answer in q_dict.items():
        res = quiz_game(s, answer, attempts)
        print(res)


if __name__ == '__main__':
    quiz_dict()

