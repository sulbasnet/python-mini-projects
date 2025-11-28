balance=0
while True:
    user=input("Would you like to 'deposit' or 'withdraw': ")
    if user=="deposit":
        depo_amount= int(input("Enter the amount: "))
        balance=balance+depo_amount
        print(f"Deposit successful. Your balance is: {balance}")
    elif user=="withdraw":
        wd_amount=int(input("Enter the amount to withdraw: "))
        if wd_amount>balance:
            print("Insufficient balance.")
        else:
            print(f"Rs. {wd_amount} is sucessfully withdrawen.")
            balance=balance-wd_amount
            print(f"Your remaining balance is: {balance}")
    else:
        print("Wrong input. Try again!")
    
    
    
    
