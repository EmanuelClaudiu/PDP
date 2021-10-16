class Account:
    
    def __init__(self, balance):
        self.balance = balance
        self.log = []

    def __str__(self):
        return f'Balance: {str(self.balance)}; Log: [{str(self.log)}]'