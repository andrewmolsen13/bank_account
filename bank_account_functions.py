from random import randint

class account:
    balance = 0.0
    
    def __init__ (self, name):
        self.account_name = name
        self.account_number = []
        while len(self.account_number)!= 5:
            self.account_number.append(randint(0,9))

    def deposit (self, amount):
        self.amount = amount
        account.balance += amount
    def withdrawl (self, amount_less):
        self.amount_less = amount_less
        account.balance -= amount_less


def menu():
    menu = [1,2,3,4]
    menu_choice = int(input("""Please choose a number:
    1. Make a deposit
    2. Make a withdrawl
    3. View Account information
    4. Quit
    """))
    while menu_choice not in menu:
        menu_choice = int(input("Invalid choice. Please enter a number 1-4. "))
    return menu_choice

def deposit_func(deposit_amount):
    account_balance = account.deposit(deposit_amount)
    return account_balance

def withdraw_func(withdraw):   
    account_balance = account.deposit(withdraw)
    return account_balance

def acc_info():
    acc_name = account.account_name
    acc_number = ''.join(account.account_number)
    acc_balance = account.balance
    return acc_name, acc_number, acc_balance
