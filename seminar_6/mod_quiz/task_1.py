# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

from math import sqrt as sq
from sys import getsizeof as size
from random import randint as rnd

x = 2
print(rnd(1, 100))
print(size(x))
print(sq(100))

