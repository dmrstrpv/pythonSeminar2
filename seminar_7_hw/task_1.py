# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

extensions_dict = {'video': ['mkv'], 'pics': ['jpeg', 'png', 'jpg'], 'text': ['txt', 'doc'], 'audio': ['mp3']}
directory = 'sem_7_tsk_4'
# os.mkdir(directory)


def mk_dir(_path: str, names: dict) -> None:
    for name in names:
        if not os.path.exists(f'{_path}\\{name}'):
            os.mkdir(f'{_path}\\{name}')


def sort_files(_path: str) -> None:
    files = [f.path for f in os.scandir(_path) if not f.is_dir()]
    extensions = list(extensions_dict.items())
    for file in files:
        ext = file.split('.')[:-1]
        name = file.split('\\')[-1]

        for key in range(len(extensions)):
            if ext in extensions[key][1]:
                os.rename(file, f'{_path}\\{extensions[key][0]}\\{name}')


mk_dir('sem_7_tsk_4', extensions_dict)
sort_files('sem_7_tsk_4')


