# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


__all__ = ['quiz_game', 'quiz_dict', 'get_stats']

_data = {}


def quiz_game(s: str, answers: str, attempts: int):
    print(s)
    cnt = 1
    while attempts > 0:
        current_try = input(f'Attempts left: {attempts}. Your answer: ')
        if current_try in answers:
            return cnt
        cnt += 1
        attempts -= 1
    else:
        return attempts


def quiz_dict(attempts: int = 3):
    q_dict = {
        'puzzle 1': ['yes', 'no'],
        'puzzle 2': ['yes', 'no'],
        'puzzle 3': ['yes', 'no']
    }

    for s, answer in q_dict.items():
        res = quiz_game(s, answer, attempts)
        add_stats(s, res)
        print(res)


def add_stats(s: str, attempts):
    _data.update({s: attempts})


def get_stats():
    print('Stats')
    output = '\n'.join((f'Puzzle {puzzle}. {f"tries {attempts}" if attempts > 0 else "Failed"}'
                        for puzzle, attempts in _data.items()))
    print(output)


if __name__ == '__main__':
    quiz_dict()
    get_stats()

