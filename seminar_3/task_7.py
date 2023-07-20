# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

input_text = input("Enter your text: ")
my_dict = {}

for sym in set(input_text):
    my_dict[sym] = input_text.count(sym)

print(my_dict)


my_dict1 = {}

for sym in input_text:
    val = my_dict1.setdefault(sym, 0)
    my_dict1[sym] += 1

print(my_dict1)

