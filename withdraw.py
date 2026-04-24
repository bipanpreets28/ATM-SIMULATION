from utils import *

def with_draw():
    unique_id = int(input("Enter your Account Number: "))
    
    if unique_id in account_number:
        i = account_number.index(unique_id)
        print(f"Greetings Mr. {username[i]}")
        
        pin = int(input("Enter your PIN: "))
        
        if pin == pins[i]:
            withd = int(input("Enter the amount to withdraw: "))
            
            if balances[i] >= withd:
                balances[i] -= withd
                transactions[i].append(f"Withdrawn: -₹{withd}")
                print(f"The amount {withd} has been withdrawn ")
            else:
                print("Insufficient Balance !!")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")