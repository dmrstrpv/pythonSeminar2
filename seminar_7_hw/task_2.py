# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


import os


def rename_files(_path: str, new_name: str, digit_num: int = 3, src_ext: str = None, dst_ext: str = None,
                 range_name: range = (3, 6)) -> None:
    cnt = 1
    for file_name in os.listdir(_path):
        if file_name.endswith(src_ext):
            scr_name = os.path.splitext(file_name)[0]
            scr_name_edit = scr_name[range_name[0]:range_name[1]] if range_name else ""
            new_file_name = f"{scr_name_edit}{new_name}{str(cnt).zfill(digit_num)}{dst_ext}"
            os.rename(os.path.join(_path, file_name), os.path.join(_path, new_file_name))
            cnt += 1


rename_files('./test_dir', 'new_file', 3, '.txt', '.doc')
