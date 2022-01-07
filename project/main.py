import json
import random
import time
from models.ticket import Ticket

file = open('inputs.json')
data = json.load(file)
file.close()

TICKETS = []

main_ticket = data

def calculateStake(matches):
    stake = 1
    for match in matches:
        stake *= float(match['stake'])
    return round(stake, 2)

TICKETS.append(Ticket(main_ticket, calculateStake(main_ticket)))

def splitIntoTwo(ticket):
    start_timer = time.time()
    minimum_difference_so_far = 1000000000
    solution = (None, None)
    while (time.time() - start_timer) < 4:
        half = len(ticket) // 2
        first_pair = ticket[:half]
        second_pair = ticket[half:]
        swapTwoRandoms(first_pair, second_pair)
        difference = abs(calculateStake(first_pair) - calculateStake(second_pair))
        if difference < minimum_difference_so_far:
            minimum_difference_so_far = difference
            start_timer = time.time()
            solution = (Ticket(first_pair, calculateStake(first_pair)), Ticket(second_pair, calculateStake(second_pair)))
    return solution


def swapTwoRandoms(first_list, second_list):
    a = first_list[random.randint(0, len(first_list) - 1)]
    b = second_list[random.randint(0, len(second_list) - 1)]
    index1 = first_list.index(a)
    index2 = second_list.index(b)
    first_list[index1] , second_list[index2] = b , a


a = splitIntoTwo(main_ticket)[0].matches
for l in splitIntoTwo(a):
    print(l.matches)
    print(f'Cota: {l.stake}')