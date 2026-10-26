from random import randint

class account:
    balance = 0.0
    
    def __init__ (self, name):
        self.account_name = name
        self.account_number = []
        while len(self.account_number)!= 5:
            self.account_number.append(str(randint(0,9)))

    def deposit (self, amount):
        self.amount = amount
        account.balance += self.amount
        return account.balance
    def withdraw (self, amount_less):
        self.amount_less = amount_less
        account.balance -= self.amount_less
        return account.balance

def menu():
    menu = [1,2,3,4]
    menu_choice = int(input("""Please choose a number:
    1. Make a deposit
    2. Make a withdrawal
    3. View Account information
    4. Quit
    """))
    while menu_choice not in menu:
        menu_choice = int(input("Invalid choice. Please enter a number 1-4. "))
    return menu_choice

def deposit_func(bank_account, deposit_amount):
    account_balance = bank_account.deposit(deposit_amount)
    return account_balance

def withdraw_func(bank_account, withdraw):
    while bank_account.balance - withdraw < 0:
        try:
            withdraw = float((input("This would put your account below 0. Please input another amount: ")))
        except ValueError:
            print("Invalid input. Pleas input a number")
    account_balance = bank_account.withdraw(withdraw)
    return account_balance

def acc_info(bank_account):
    acc_name = bank_account.account_name
    acc_number = ''.join(bank_account.account_number)
    acc_balance = bank_account.balance
    return acc_name, acc_number, acc_balance
