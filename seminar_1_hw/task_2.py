# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


SPACE = "     "

print("\n")
for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j} * {i} = {i * j}\t", end=SPACE)
    print(SPACE)
print("\n")

for i in range(2, 11):
    for j in range(6, 10):
        print(f"{j} * {i} = {i * j}\t", end=SPACE)
    print(SPACE)
