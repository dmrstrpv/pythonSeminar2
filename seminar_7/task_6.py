# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import task_4
import task_5
import os


def is_dir(_path: str, **kwargs) -> None:
    if not os.path.exists(_path):
        os.mkdir(_path)

    os.chdir(_path)
    task_5.extensions(**kwargs)


is_dir(r".\\test_dir", gif=9, doc=3, txt=5, jpeg=6)

