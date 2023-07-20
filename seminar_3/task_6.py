# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


some_text = input("Enter your text here: ")
some_list = sorted(some_text.split(" "))

max_len = 0
for word in some_list:
    if len(word) > max_len:
        max_len = len(word)

for num, word in enumerate(some_list, start=1):
    print(f'{num}. {word:>{max_len}}')


