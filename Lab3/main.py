#!/usr/bin/python

from threading import Thread, Lock
import random

MATRIX_ROWS = 9
MATRIX_COLUMNS = 9
MAXIMUM_ELEMENT = 1

ORDER = []

def initialize_matrix(matrix):
    for row in range(1, MATRIX_ROWS + 1):
        row_vector = []
        for column in range(1, MATRIX_COLUMNS + 1):
            row_vector.append(random.randint(1, MAXIMUM_ELEMENT))
        matrix.append(row_vector)

matrix1 = []
matrix2 = []
initialize_matrix(matrix1)
initialize_matrix(matrix2)

THREADS = []
FINAL_MATRIX = []

mutex = Lock()
class myThread (Thread):

    def __init__(self, row):
        Thread.__init__(self)
        self.row = row
        self.result_row = []

    def run(self):
        global MATRIX_COLUMNS
        for column in range(1, MATRIX_COLUMNS + 1):
            element = 0
            for index in range(1, MATRIX_COLUMNS + 1):
                # mutex.acquire()
                element += matrix1[self.row - 1][index - 1] * matrix2[index - 1][column - 1]
                # mutex.release()
            self.result_row.append(element)
        self.appendToGlobalMatrix()
    
    def appendToGlobalMatrix(self):
        appended = False
        while not appended:
            mutex.acquire()
            if len(ORDER) == 0 and self.row == 1:
                ORDER.append(self.row)
                FINAL_MATRIX.append(self.result_row)
                appended = True
            else:
                if ORDER[-1] == (self.row - 1):
                    ORDER.append(self.row)
                    FINAL_MATRIX.append(self.result_row)
                    appended = True     
            mutex.release()
  
for row in range(1, MATRIX_ROWS + 1):
    thread = myThread(row)
    THREADS.append(thread)

for thread in THREADS:
    thread.run()

while len(ORDER) < len(THREADS):
    pass

for row in matrix1:
    print(row)
    
print("--------------------")
    
for row in matrix2:
    print(row)
    
print("--------------------")

for row in FINAL_MATRIX:
    print(row)