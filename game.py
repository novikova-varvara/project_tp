from bank import *

class Game:
    def __init__(self):
        self.bank = Bank()
        self.flag = True
    def run(self):
        while self.flag == True:
            print("Hello! What do you want to do?", "1.Become a client", "2.Put money on the card", "3.Withdraw money from the card", "4.Transfer money", "5.Set address", "6.Set passport", "7.Check balance", "8.Cancel operation", "9.End the banking session", "Please, print the required number", sep='\n')
            num = check_type_int(input())

            if num == 1:
                print("Please, choose type of account: debit, deposit or credit. Print the required type")
                typ = str(input())
                if typ == "":
                    print("Invalid data type")
                    continue
                self.bank.create_new_account(typ)

            elif num == 2:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                print("Please, print the amount of money, you want to deposit")
                sum = check_type_int(input())
                if sum == "":
                    continue
                self.bank.add_cash(ID, sum)

            elif num == 3:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                print("Please, print the amount of money, you want to withdraw")
                sum = check_type_int(input())
                if sum == "":
                    continue
                self.bank.withdraw_cash(ID, sum)

            elif num == 4:
                print("Please, print your ID")
                ID_from = check_type_int(input())
                if ID_from == "":
                    continue
                print("Please, print ID, where to transfer money")
                ID_to = check_type_int(input())
                if ID_to == "":
                    continue
                print("Please, print the amount of money, you want to transfer")
                sum = check_type_int(input())
                if sum == "":
                    continue
                self.bank.transfer_cash(ID_to, ID_from, sum)

            elif num == 5:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                print("Please, print your passport")
                passport = str(input())
                if passport == "":
                    print("Invalid type")
                    continue
                self.bank.set_passport(ID, passport)

            elif num == 6:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                print("Please, print your address")
                address = str(input())
                if address == "":
                    print("Invalid type")
                    continue
                self.bank.set_address(ID, address)

            elif num == 7:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                self.bank.print_balance(ID)

            elif num == 8:
                print("Please, print your ID")
                ID = check_type_int(input())
                if ID == "":
                    continue
                self.bank.print_history(ID)
                print("Please, print the number of operation")
                num = check_type_int(input())
                if num == "":
                    continue
                self.bank.cancel_operation(ID, num)

            elif num == 9:
                print("Goodbye!")
                self.flag = False

            else:
                print("Invalid number")