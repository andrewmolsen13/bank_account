from bank_account_functions import *

print("Welcome to Olsen bank!")
account_name = input("What is your first and last name? ")

account1 = account(account_name)
logged_in = True
while logged_in:
    menu_choice = menu()

    if menu_choice == 1:
        deposit_amount = int(input("How much would you like to deposit? "))
        account_balance = deposit_func(deposit_amount)
        print()
    elif menu_choice == 2:
        withdraw = int(input("How much would you like to withdraw? "))
        account_balance = withdraw_func(withdraw)
    elif menu_choice == 3:
        acc_name, acc_number, acc_balance = acc_info()
        print(f"""Account Name: {acc_name}
        Account #: {acc_number}
        Account Balance: {acc_balance}""")
    elif menu_choice == 4:
        logged_in = False
print("Thank you for visiting!")