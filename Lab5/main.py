from threading import Thread, Lock

A = [5, 0, 10, 6]
#   5 + 0x^1 + 10x^2 + 6x^3

polynomial_1 = [5, 0, 10, 6]
polynomial_2 = [1, 2, 4]

product = []

mutex = Lock()

def initialize_product():
    global product, polynomial_1, polynomial_2
    for i in range (1, len(polynomial_1) + len(polynomial_2)):
        product.append(0)

initialize_product()

THREADS = []

class myThread(Thread):

    def __init__(self, index):
        Thread.__init__(self)
        self.i = index

    def run(self):
        global product, polynomial_1, polynomial_2
        for j in range(0, len(polynomial_2)):
            product[(self.i + j)] = product[(self.i + j)] + (polynomial_1[self.i] * polynomial_2[j])

for index in range(0, len(polynomial_1)):
    thread = myThread(index)
    THREADS.append(thread)

for thread in THREADS:
    thread.run()

print(product)