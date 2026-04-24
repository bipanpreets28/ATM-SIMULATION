from deposit import *
from withdraw import with_draw
from balance import show_bal
from utils import *
from statement import *

print("Hey there , Welcome to this ATM Simulation")

while True:
    
    print("\nWithdraw Cash --> [1]")
    print("Check Balance --> [2]")
    print("Deposit Money --> [3]")
    print("Check Bank Statements --> [4]")
    print("Exit ATM --> [5]")

    response = int(input(">>> "))

    if response == 1:
        with_draw()

    elif response == 2:
        show_bal()

    elif response == 3:
        deposits()

    elif response == 4:
        check_statement()

    elif response == 5:
        print(f"Thank you :)")
        break

    else:
        print("Please enter a valid input between numbers 1-5")