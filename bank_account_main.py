from bank_account_functions import *

print("Welcome to Olsen bank!")
account_name = input("What is your first and last name? ")

account1 = account(account_name)
logged_in = True
while logged_in:
    menu_choice = menu()

    if menu_choice == 1:
        deposit_amount = int(input("How much would you like to deposit? "))
        account_balance = deposit_func(account1, deposit_amount)
        print(f"Your account balance is ${account_balance:.2f}")
    elif menu_choice == 2:
        withdraw = int(input("How much would you like to withdraw? "))
        account_balance = withdraw_func(account1, withdraw)
        print(f"Your account balance is ${account_balance:.2f}")
    elif menu_choice == 3:
        acc_name, acc_number, acc_balance = acc_info(account1)
        print(f"""Account Name: {acc_name} \nAccount #: {acc_number} \nAccount Balance: {acc_balance}""")
    elif menu_choice == 4:
        logged_in = False
print("Thank you for visiting!")