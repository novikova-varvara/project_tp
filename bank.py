from accounts import *
from commands import *
from client import *
from check import *
class Bank:
    def __init__(self):
        self.bank_accounts = dict()
        self.clients = dict()
        self.next_num = 0
    def create_new_account(self, typ):
        if typ == "debit":
            new_account = DebitAccount(self.next_num)
        elif typ == "credit":
            new_account = CreditAccount(self.next_num)
        elif typ == "deposit":
            new_account = DepositAccount(self.next_num)
        else:
            print("Invalid type of account")
            return
        self.create_new_client(new_account)
    def create_new_client(self, account):
        print("Enter your name")
        name = str(input())
        if name == "":
            print("Invalid data type")
            return

        print("Enter your surname")
        surname = str(input())
        if surname == "":
            print("Invalid data type")
            return

        print("Enter your address or press ENTER")
        address = str(input())
        if address == "":
            address = None

        print("Enter your passport or press ENTER")
        passport = str(input())
        if passport == "":
            passport = None

        client = Client()
        client = client.builder(self.next_num)\
            .set_name(name)\
            .set_surname(surname)\
            .set_address(address)\
            .set_passport(passport)\
            .build()
        self.bank_accounts[self.next_num] = account
        self.clients[client.num] = client
        self.next_num += 1
        print("Please, remember your ID", " - ", client.num, sep='')
    def add_cash(self, num_account, sum):
        if check_num(num_account, self.next_num):
            account = self.bank_accounts[num_account]

            type = account.type
            if type == "deposit":
                comm_dep = CommandDep()
                comm_dep.add_cash(account, sum)
            elif type == "debit":
                comm_deb = CommandDeb()
                comm_deb.add_cash(account, sum)
            elif type == "credit":
                comm_cre = CommandCre()
                comm_cre.add_cash(account, sum)
    def withdraw_cash(self, num_account, sum):
            if check_num(num_account, self.next_num):
                account = self.bank_accounts[num_account]
                flag = self.clients[num_account].check_flag()
                if flag == False and sum > self.clients[num_account].limit:
                    print("Invalid operation. Please, set your client data")
                    return

                type = account.type
                if type == "deposit":
                    comm_dep = CommandDep()
                    comm_dep.withdraw_cash(account, sum)
                elif type == "debit":
                    comm_deb = CommandDeb()
                    comm_deb.withdraw_cash(account, sum)
                elif type == "credit":
                    comm_cre = CommandCre()
                    comm_cre.withdraw_cash(account, sum)
    def transfer_cash(self, num_account_to, num_account_from, sum):
        if check_num(num_account_to, self.next_num) and check_num(num_account_from, self.next_num):
            account_to = self.bank_accounts[num_account_to]
            account_from = self.bank_accounts[num_account_from]
            flag = self.clients[num_account_from].check_flag()
            if flag == False and sum > self.clients[num_account_from].limit:
                print("Invalid operation. Please, set your client data")
                return

            type = account_from.type
            if type == "deposit":
                comm_dep = CommandDep()
                comm_dep.transfer_cash(account_to, account_from, sum)
            elif type == "debit":
                comm_deb = CommandDeb()
                comm_deb.transfer_cash(account_to, account_from, sum)
            elif type == "credit":
                comm_cre = CommandCre()
                comm_cre.transfer_cash(account_to, account_from, sum)
    def set_passport(self, num_account, passport):
        if check_num(num_account, self.next_num):
            client = self.clients[num_account]
            self.clients[num_account] = client.modifier(num_account).set_passport(passport).build()
    def set_address(self, num_account, address):
        if check_num(num_account, self.next_num):
            client = self.clients[num_account]
            self.clients[num_account] = client.modifier(num_account).set_address(address).build()
    def print_balance(self, num_account):
        if check_num(num_account, self.next_num):
            account = self.bank_accounts[num_account]
            print(account.balance)
    def cancel_operation(self, num_account, num_operation):
        if check_num(num_account, self.next_num):
            account_from = self.bank_accounts[num_account]
            if check_num(num_operation, account_from.count):
                sum = account_from.history[num_operation][1]
                account_to = account_from.history[num_operation][0]
                if account_to == None:
                    self.add_cash(num_account, -sum)
                else:
                    self.add_cash(account_to, sum)
                    self.add_cash(num_account, -sum)
    def print_history(self, num_account):
        if check_num(num_account, self.next_num):
            account = self.bank_accounts[num_account]
            copy = account.count - 1
            while copy > 0:
                if account.history[copy][0] == None:
                    print(copy, '. Add/withdraw ', account.history[copy][1], ' money', sep='')
                elif account.history[copy][1] < 0:
                    print(copy, '. Transfer to ', account.history[copy][0], ' ', -account.history[copy][1], ' money', sep='')
                else:
                    print(copy, '. Get money from ', account.history[copy][0], ' ', account.history[copy][1], ' money', sep='')
                copy -= 1