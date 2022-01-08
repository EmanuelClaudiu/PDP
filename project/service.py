import json
import random
import time

class TicketSPlitService:

    def __init__(self, input):
        if input == None:
            file = open('inputs.json')
            data = json.load(file)
            file.close()
        else:
            data = input
        self.TICKETS = []
        self.main_ticket = data
        self.TICKETS.append(self.main_ticket)
        a = self.splitIntoTwo(self.main_ticket)
        for t in a:
            self.splitIntoTwo(t)

    def calculateStake(self, matches):
        stake = 1
        for match in matches:
            stake *= float(match['stake'])
        return round(stake, 2)

    def swapTwoRandoms(self, first_list, second_list):
        a = first_list[random.randint(0, len(first_list) - 1)]
        b = second_list[random.randint(0, len(second_list) - 1)]
        index1 = first_list.index(a)
        index2 = second_list.index(b)
        first_list[index1], second_list[index2] = b, a

    def splitIntoTwo(self, ticket):
        start_timer = time.time()
        minimum_difference_so_far = 1000000000
        solution = (None, None)
        while (time.time() - start_timer) < 4:
            half = len(ticket) // 2
            first_pair = ticket[:half]
            second_pair = ticket[half:]
            self.swapTwoRandoms(first_pair, second_pair)
            difference = abs(self.calculateStake(first_pair) - self.calculateStake(second_pair))
            if difference < minimum_difference_so_far:
                minimum_difference_so_far = difference
                start_timer = time.time()
                solution = (first_pair, second_pair)
        self.TICKETS.append(solution[0])
        self.TICKETS.append(solution[1])
        return solution

    def prettyPrint(self):
        for ticket in self.TICKETS:
            print(f"----------Ticket nr: {self.TICKETS.index(ticket) + 1}----------")
            for match in ticket:
                print(f'{match["tag"]} - {match["bet"]} - {match["stake"]}')
            print(f"--Stake: {self.calculateStake(ticket)}")