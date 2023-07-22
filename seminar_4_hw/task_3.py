# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def my_dict_func(**kwargs) -> dict:
    my_dict = {}
    for key, value in kwargs.items():
        try:
            _ = hash(value)
            my_dict[value] = key
        except TypeError:
            my_dict[key] = value

    return my_dict


print(my_dict_func(food=1, torch=2, sleeping_bag=3, tent=4, stove=5, hiking_boots=6))

