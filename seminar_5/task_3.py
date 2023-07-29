# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

ITER_NUM = 5

s: str = "This is some text"
dict_text: dict = {key: ord(key) for key in s}
print(dict_text)

iteration = iter(dict_text.items())
for _ in range(ITER_NUM):
    print(next(iteration))

    