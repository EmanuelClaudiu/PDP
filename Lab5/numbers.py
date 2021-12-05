from threading import Thread, Lock

a = 4526
b = 347
print(a*b)

SUM_POOL = []
class myThread(Thread):

    def __init__(self, a, b, index):
        Thread.__init__(self)
        self.index = index
        self.a = a
        self.b = b
        self.in_memory = 0
        self.step = 1
        self.result = 0

    def run(self):
        global SUM_POOL
        while self.a != 0:
            term1 = self.a % 10
            term2 = self.b
            p = term1 * term2
            p += self.in_memory
            to_add = p % 10
            to_add = to_add % 10
            self.result = self.result + (to_add * self.step)
            self.in_memory = (p // 10)
            self.a //= 10
            self.step *= 10
        if self.in_memory != 0:
            self.result += self.in_memory * self.step
        SUM_POOL.append(self.result * (10 ** self.index))

def number_length(a):
    return len(str(a))

n = number_length(b)

for i in range(0, n):
    thread = myThread(a, b%10, i)
    thread.run()
    b //= 10
    
FINAL_PRODUCT = 0

for term in SUM_POOL:
    FINAL_PRODUCT += term
    
print(FINAL_PRODUCT)
