#!/usr/bin/python

from threading import Thread, Lock
import random

MAXIMUM_VECTOR_SIZE = 30
MAXIMUM_ELEMENT_SIZE = 5

PRODUCT_VECTOR = []

SUM = 0

# construct a random vector
def initialize_vector():
    data = []
    for i in range(1, MAXIMUM_VECTOR_SIZE):
        data.append(random.randint(1, MAXIMUM_ELEMENT_SIZE))
    return data

mutex = Lock()
producer_started = False

producer_ended = False
consumer_ended = False

first_vector = initialize_vector()
second_vector = initialize_vector()

class ProducerThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("[PRODUCER] Starting producer thread")
        global producer_started
        global producer_ended
        global PRODUCT_VECTOR
        producer_started = True
        for item1 in first_vector:
            for item2 in second_vector:
                mutex.acquire()
                print(f"[PRODUCER] Made a product")
                PRODUCT_VECTOR.append(item1 * item2)
                mutex.release()
        producer_ended = True
        print("[PRODUCER] Exiting producer thread")

class ConsumerThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("[CONSUMER] Starting consumer thread")
        global producer_started
        global producer_ended
        global consumer_ended
        global PRODUCT_VECTOR
        global SUM

        while producer_ended == False:
            # two cases
            # producer still runs
            if producer_started == True:
                if len(PRODUCT_VECTOR) > 0:
                    mutex.acquire()
                    item = PRODUCT_VECTOR.pop()
                    print(f"[CONSUMER] Consumer popped item from PRODUCT_VECTOR")
                    SUM = SUM + item
                    print(f"[CONSUMER] Made a sum")
                    mutex.release()
            # producer is done
            while(len(PRODUCT_VECTOR) > 0):
                mutex.acquire()
                item = PRODUCT_VECTOR.pop()
                print(f"[CONSUMER] Consumer popped item from PRODUCT_VECTOR")
                SUM = SUM + item
                print(f"[CONSUMER] Made a sum")
                mutex.release()
        consumer_ended = True
        print("[CONSUMER] Exiting consumer thread")

producer = ProducerThread()
consumer = ConsumerThread()

producer.start()
print(f"[MAIN THREAD] Started producer thread")
consumer.start()
print(f"[MAIN THREAD] Started consumer thread")

while consumer_ended == False:
    pass

print(f"[MAIN THREAD] First vector: {first_vector}")
print(f"[MAIN THREAD] Second vector: {second_vector}")
print(f"[MAIN THREAD] Scalar Product = {SUM}")
print("[MAIN THREAD] Exiting main thread")