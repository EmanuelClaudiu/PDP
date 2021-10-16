#!/usr/bin/python

from threading import Thread, Lock
import random
from models.account import Account
from models.record import Record

NUMBER_OF_ACCOUNTS = 0
NUMBER_OF_THREADS = 0

ACCOUNTS = []

def read_number_of_accounts():
   global NUMBER_OF_ACCOUNTS 
   try:
      print("How many accounts are there?")
      NUMBER_OF_ACCOUNTS = int(input(">> "))
   except ValueError as e:
      read_number_of_accounts()

def read_number_of_threads():
   global NUMBER_OF_THREADS
   try:
      print("How many threads are there?")
      NUMBER_OF_THREADS = int(input(">> "))
   except ValueError as e:
      read_number_of_threads()

read_number_of_accounts()
read_number_of_threads()

def pick_random_balance():
   return random.randint(0, 10000)

for i in range(1, NUMBER_OF_ACCOUNTS + 1):
   ACCOUNTS.append(Account(pick_random_balance()))

