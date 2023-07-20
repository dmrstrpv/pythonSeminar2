# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

import decimal


def get_rates(names: list[str], bets: list[int], rates: list[str]) -> dict[str: decimal.Decimal]:
    print(list(zip(names, bets, rates)))
    people = {}
    for name, bet, rate in zip(names, bets, rates):
        people[name] = bet * decimal.Decimal(rate[:-1]) / 100
    return people


names = ['Петя', 'Вася', 'Ваня', 'Ирина']
bets = [10_000, 25_000, 14_000, 17_500]
rates = ['9,5%', '7,85%', '12.33%', '16,66%']

print(get_rates(names, bets, rates))

