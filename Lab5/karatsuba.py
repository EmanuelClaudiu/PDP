from threading import Thread, Lock

a = 4526
b = 347
print(a*b)

class karatsubaThread(Thread):

    def __init__(self, x, y):
        Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        if self.x < 10 or self.y < 10:
            return self.x * self.y
        else:
            n = max(self.number_length(self.x), self.number_length(self.y))
            half = n // 2
            # x = a|b
            # y = c|d
            a = self.x // (10 ** (half)) # left part of x
            b = self.x % (10 ** (half)) # right part of x
            c = self.y // (10 ** (half)) # left part of y
            d = self.y % (10 ** (half)) # right part of y
            thread1 = karatsubaThread(a, c)
            thread2 = karatsubaThread(b, d)
            thread3 = karatsubaThread(a+b , c+d)
            ac = thread1.run()
            bd = thread2.run()
            ad_plus_bc = thread3.run() - ac - bd
            # formula: x * y = [ac * 10^(2(n/2))] + [(ad + bc) * 10^(n/2)] + bd
            return (ac * (10 ** (2 * half))) + (ad_plus_bc * (10 ** half)) + bd

    def number_length(self, number):
        return len(str(number))

thread = karatsubaThread(a, b)
print(thread.run())