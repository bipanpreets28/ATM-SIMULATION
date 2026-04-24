from utils import *

def show_bal():
    account_no = int(input("Enter your Account Number: "))
    
    if account_no in account_number:
        i = account_number.index(account_no)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == pins[i]:
            balancee = balances[i]
            print(f"Available Balance is: {balancee}")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Account Number !!!,try again with correct account number")