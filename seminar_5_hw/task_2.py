# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


s: str = "https://gbcdn.mrgcdn.ru/uploads/asset/4920278/attachment/0335f62338b12e3dbd73c961bffecf19.pdf"


def foo(input_str: str):
    *path, file = s.split('/')
    path_ = '/'.join(path)
    file_name, file_extension = file.split('.')
    result = (path_, file_name, file_extension)
    print(result)


foo(s)
