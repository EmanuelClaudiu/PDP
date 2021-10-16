import random

class Account:
    
    def __init__(self, balance):
        self.balance = balance
        self.log = []

    def transfer(self, another_account):
        amount = random.randint(1, 100)
        if amount > self.balance:
            # not enough funds
            return { "succes": False, "message": "Not enough funds in your account" }
        else:
            initial_source_balance = self.balance
            initial_destination_balance = another_account.balance
            self.balance = self.balance - amount
            another_account.balance += amount
            return { "succes": True, "message": "Funds transfered succesfully",
                    "amount": amount, "source": self, "destination": another_account, 
                    "pre_source": initial_source_balance, "pre_destination": initial_destination_balance }

    def __str__(self):
        return f'Balance: {str(self.balance)}; Log: [{str(self.log)}]'
        