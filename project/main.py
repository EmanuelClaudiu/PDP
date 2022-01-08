import json
import random
import time

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

TICKETS.append(main_ticket)

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
            solution = (first_pair, second_pair)
    TICKETS.append(solution[0])
    TICKETS.append(solution[1])
    return solution


def swapTwoRandoms(first_list, second_list):
    a = first_list[random.randint(0, len(first_list) - 1)]
    b = second_list[random.randint(0, len(second_list) - 1)]
    index1 = first_list.index(a)
    index2 = second_list.index(b)
    first_list[index1] , second_list[index2] = b , a


a = splitIntoTwo(main_ticket)
for t in a:
    splitIntoTwo(t)

for ticket in TICKETS:
    print(f"----------Ticket nr: {TICKETS.index(ticket) + 1}----------")
    for match in ticket:
        print(f'{match["tag"]} - {match["bet"]} - {match["stake"]}')
    print(f"--Stake: {calculateStake(ticket)}")