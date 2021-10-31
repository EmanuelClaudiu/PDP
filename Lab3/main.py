#!/usr/bin/python

from threading import Thread, Lock
import random

MATRIX_ROWS = 3
MATRIX_COLUMNS = 3
MAXIMUM_ELEMENT = 9

def initialize_matrix(matrix):
    for row in range(1, MATRIX_ROWS + 1):
        row_vector = []
        for column in range(1, MATRIX_COLUMNS + 1):
            row_vector.append(random.randint(1, MAXIMUM_ELEMENT))
        matrix.append(row_vector)

matrix = []
initialize_matrix(matrix)
for row in matrix:
    print(row)