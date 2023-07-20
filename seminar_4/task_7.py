# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.




def comp_analysis(data: dict[str, list[int]]) -> bool:
    # is_all_profitable = False
    # for money_flows in companies.values():
    #     if sum(money_flows) < 0:
    #         return False
    # return True
    map(lambda x: sum(x) > 0, data.values())
    


companies = {
    'samsung': [100, -300, 1200, 500],
    'apple': [100, -30, -500, 10000],
    'google': [-900, -300, 447, 3000],
    'haier': [1000, -300, 200, 100],
    'panasonic': [100, -3000, 1200, 3456],
}

print(comp_analysis(companies))

