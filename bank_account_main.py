from bank_account_functions import *

print("Welcome to Olsen bank!")
account_name = input("What is your first and last name? ")

account1 = account(account_name)
logged_in = True
while logged_in:
    menu_choice = menu()

    if menu_choice == 1:
        valid_amount = False
        
        while not valid_amount:
            try:
                deposit_amount = float(input("How much would you like to deposit? "))
                
                if deposit_amount < 0:
                    print("Please input a positive amount")
                else:
                    valid_amount = True
            except ValueError:
                print("Invalid input. Please input a number")

        account_balance = deposit_func(account1, deposit_amount)
        print(f"Your account balance is ${account_balance:.2f}")
    
    elif menu_choice == 2:
        valid_amount = False

        while not valid_amount:
            try:
                withdraw = float(input("How much would you like to withdraw? "))
                
                if withdraw < 0:
                    print("Please input a positive amount")
                else:
                    valid_amount = True
            except ValueError:
                print("Invalid input. Please input a number")

        account_balance = withdraw_func(account1, withdraw)
        print(f"Your account balance is ${account_balance:.2f}")
    
    elif menu_choice == 3:
        acc_name, acc_number, acc_balance = acc_info(account1)
        print(f"""Account Name: {acc_name} \nAccount #: {acc_number} \nAccount Balance: {acc_balance:.2f}""")
    
    elif menu_choice == 4:
        logged_in = False
print("Thank you for visiting!")