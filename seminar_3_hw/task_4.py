# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

camp_gear = {'food': 5, 'torch': 0.2, 'sleeping bag': 1, 'tent': 8, 'stove': 2, 'hiking boots': 2}
backpack = 15


def knapsack_problem(max_weight: int, gear: dict) -> list[str]:
    best_solution = []
    for key, value in gear.items():
        if value < max_weight:
            max_weight -= value
            best_solution.append(key)
    return best_solution


print(knapsack_problem(backpack, camp_gear))