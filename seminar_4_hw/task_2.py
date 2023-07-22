# Напишите функцию для транспонирования матрицы

import numpy

mtrx = ([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])
new_matrix = numpy.transpose(mtrx)


def transpose_matrix(matrix: list[list]) -> list[list]:
    matrix = [[0 for j in range(len(mtrx))] for i in range(len(mtrx[0]))]
    for row in range(0, len(mtrx)):
        for col in range(len(mtrx[row])):
            matrix[row][col] = mtrx[col][row]
    return matrix


def print_matrix(matrix: list[list]):
    for i in matrix:
        print(i)


print("Matrix")
print_matrix(mtrx)
print()
print("Transposed matrix")
print_matrix(transpose_matrix(mtrx))

