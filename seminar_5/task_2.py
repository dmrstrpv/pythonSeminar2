# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

text: str = "This is some text"

print(ord("T"))
print(dict(enumerate(text)))

s: str = "This is some text"
dict_text: dict = {key: ord(key) for key in s}
print(dict_text)

dict_text_2 = {}
for i in s:
    dict_text_2[i] = ord(i)
print(dict_text_2)

