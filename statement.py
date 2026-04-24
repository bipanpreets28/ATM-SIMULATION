from utils import *

def check_statement():
    unique_id = int(input("Enter your Account Number: "))
    
    if unique_id in account_number:
        i = account_number.index(unique_id)
        print(f"Greetings Mr. {username[i]}")
        
        pin = int(input("Enter your PIN: "))
        
        if pin == pins[i]:
            print("\n--- Bank Statement ---")
            
            
            history = transactions[i]
            
           
            if len(history) == 0:
                print("No recent transactions.")
            else:
               
                for record in history:
                    print(record)
            
            print(f"----------------------")
            print(f"Current Balance: ₹{balances[i]}\n")
            
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")