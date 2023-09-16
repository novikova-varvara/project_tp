class Account:
    def __init__(self):
        self.num = None
        self.type = None
        self.balance = None
        self.history = dict()
        self.count = None
class DebitAccount(Account):
    def __init__(self, num):
        self.num = num
        self.type = "debit"
        self.balance = 0
        self.history = dict()
        self.count = 1
class CreditAccount(Account):
    def __init__(self, num):
        self.num = num
        self.type = "credit"
        self.balance = 0
        self.percent = 1
        self.limit = -15000
        self.history = dict()
        self.count = 1
class DepositAccount(Account):
    def __init__(self, num):
        self.num = num
        self.type = "deposit"
        self.balance = 0
        self.history = dict()
        self.count = 1