from abc import abstractmethod
class Command:
    @abstractmethod
    def add_cash(self, account, sum):
        pass
    @abstractmethod
    def withdraw_cash(self, account, sum):
        pass
    @abstractmethod
    def transfer_cash(self, account_to, account_from, sum):
        pass
    @staticmethod
    def update_history(account_to, account_from, sum):
        if account_to == None:
            account_from.history[account_from.count] = (None, sum)
            account_from.count += 1
        else:
            account_to.history[account_to.count] = (account_from.num, sum)
            account_from.history[account_from.count] = (account_to.num, -sum)
            account_to.count += 1
            account_from.count += 1
class CommandDeb(Command):
    def add_cash(self, account, sum):
        account.balance += sum
        Command.update_history(None, account, sum)
    def withdraw_cash(self, account, sum):
        if account.balance >= sum:
            account.balance -= sum
            Command.update_history(None, account, -sum)
        else:
            print("Invalid operation: not enough money")
    def transfer_cash(self, account_to, account_from, sum):
        if account_from.balance >= sum:
            if account_to.type == "credit" and account_to.balance < 0:
                account_to.balance += account_to.balance * account_to.percent
            account_to.balance += sum
            account_from.balance -= sum
            Command.update_history(account_to, account_from, sum)
        else:
            print("Invalid operation: not enough money")
class CommandDep(Command):
    def add_cash(self, account, sum):
        account.balance += sum
        Command.update_history(None, account, sum)
    def withdraw_cash(self, account, sum):
        print("Invalid operation: cannot withdraw money")
    def transfer_cash(self, account_to, account_from, sum):
        print("Invalid operation: cannot transfer money")

class CommandCre(Command):
    def add_cash(self, account, sum):
        if account.balance < 0:
            account.balance -= account.balance * account.percent
        account.balance += sum
        Command.update_history(None, account, sum)
    def withdraw_cash(self, account, sum):
        if account.balance - sum >= account.limit:
            account.balance -= sum
            Command.update_history(None, account, -sum)
        else:
            print("Invalid operation: limit is exceeded")
    def transfer_cash(self, account_to, account_from, sum):
        if account_from.balance - sum >= account_from.limit:
            if account_to.type == "credit" and account_to.balance < 0:
                account_to.balance += account_to.balance * account_to.percent
            account_to.balance += sum
            account_from.balance -= sum
            Command.update_history(account_to, account_from, sum)
        else:
            print("Invalid operation: limit is exceeded")