#!/usr/bin/python

from threading import Thread, Lock
import random
import pickle
import time
from models.account import Account
from models.record import Record

# these will store data read from the user
NUMBER_OF_ACCOUNTS = 0
NUMBER_OF_THREADS = 0

LAST_RECORD = -1

# this will store data shared by the threads (list of accounts)
ACCOUNTS = []

# this will be a list of all threads
THREADS = []

# function for no. of accounts input
def read_number_of_accounts():
   global NUMBER_OF_ACCOUNTS 
   try:
      print("How many accounts are there?")
      NUMBER_OF_ACCOUNTS = int(input(">> "))
   except ValueError as e:
      read_number_of_accounts()

# function for no. of threads input
def read_number_of_threads():
   global NUMBER_OF_THREADS
   try:
      print("How many threads are there?")
      NUMBER_OF_THREADS = int(input(">> "))
   except ValueError as e:
      read_number_of_threads()

# reads no. of accounts + no. of threads
read_number_of_accounts()
read_number_of_threads()

# picks random balance
def pick_random_balance():
   return random.randint(0, 10000)

# generates the list of accounts
for i in range(1, NUMBER_OF_ACCOUNTS + 1):
   ACCOUNTS.append(Account(pick_random_balance()))

mutex = Lock()

def consistency_check():

   errors = []

   global ACCOUNTS

   for account in ACCOUNTS:
      if len(account.log) == 0:
         pass
      else:
         current_balance = account.balance
         first_log = account.log[0]
         initial_balance = 0
         if first_log.source is account:
            initial_balance = first_log.source_before
         else:
            initial_balance = first_log.destination_before

         for record in account.log:
            # two cases: money received and money sent
            if record.source is account:
               # money was sent from account => account is record.source
               if record not in record.destination.log:
                  errors.append(f'Record with id={record.id} could not be found in destination{record.destination}')
               initial_balance -= record.amount
            else:
               # money was received by account => account is record.destiantion
               if record not in record.source.log:
                  errors.append(f'Record with id={record.id} could not be found in source{record.source}')
               initial_balance += record.amount

         if initial_balance != current_balance:
            errors.append(f'Account {account} does not have the same current balance as the logs indicate')
   
   if len(errors) == 0:
      print()
      print("----------------------------------------------------------")
      print("[Success] Consistency check performed. Everything is good.")
      print("----------------------------------------------------------")
      print()
      return True
   else:
      print("[ERROR] Consistency check performed. Error(s) found:")
      print(errors)
      return False

TO_PRINT = []

def do_transaction(thread):
   mutex.acquire()

   global ACCOUNTS
   global LAST_RECORD
   
   first_account = ACCOUNTS[random.randint(0, len(ACCOUNTS) - 1)]
   second_account = ACCOUNTS[random.randint(0, len(ACCOUNTS) - 1)]
   
   if first_account is not second_account:
      response = first_account.transfer(second_account)

      if response["succes"] == True:
         LAST_RECORD += 1
         record = Record(LAST_RECORD, response["source"], response["destination"],
                        response["pre_source"] , response["pre_destination"] , response["amount"])
         first_account.log.append(record)
         second_account.log.append(record)

         print(f'{thread.name}: Transaction success: {response}')
   
   mutex.release()

# thread implementation
class myThread (Thread):

   def __init__(self, threadID, name, counter):
      Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print("Starting " + self.name)
      while True:
         time.sleep(random.randint(3, 4))
         do_transaction(self)
      print("Exiting " + self.name)

# initializing threads
for i in range(1, NUMBER_OF_THREADS + 1):
   thread = myThread(i, f'Thread-{i}', 3 + i)
   THREADS.append(thread)

for thread in THREADS:
   thread.start()

# the interval at which consistency check is performed (in seconds)
CONSISTENCY_CHECK_INTERVAL = 5

flag = True
while flag:
   time.sleep(CONSISTENCY_CHECK_INTERVAL)
   mutex.acquire()
   feedback = consistency_check()
   # here we should store all logs somewhere and then flush them
   for account in ACCOUNTS:
      # TODO: store logs state somewhere
      # TODO: put a mutex on the account when doing the transaction, so it can be asynchronous
      account.log = []
   mutex.release()
   if not feedback:
      flag = False
      