from utils import *

def deposits():
    unique_id = int(input("Enter your Unique User Id: "))
    
    # Check if the ID exists in the list
    if unique_id in account_number:
        # Get the exact index of the user
        i = account_number.index(unique_id)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        # Check the PIN at that exact same index
        if unique_pinn == pins[i]:
            deposit = int(input("Enter the amount to deposit: "))
            balances[i] += deposit
            transactions[i].append(f"Deposited: +₹{deposit}")

            print(f"The amount {deposit} has been deposited to your account")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")