# Banking Problem 

import time

class Account:
    def __init__(self, name, accnum, pword):
        self.name = name
        self.accnum = accnum
        self.pword = pword
        self.balance = 0
        
    def deposit(self, balance, accnum):
        if self.accnum == accnum and balance > 0:
            self.balance += balance
            print(f"Deposited {balance} to account {self.accnum}")
        else:
            print("Invalid deposit amount")
            
    def withdraw(self, balance, accnum, pword):
        if self.accnum == accnum and self.pword == pword:
            if balance <= self.balance:
                self.balance -= balance
                print(f"Withdrew {balance} from account {self.accnum}")
                print(f"Avaiable balance: {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid account number or password")
            
    def changepassword(self, oldpword, newpword,accnum):
        if self.accnum == accnum and self.pword == oldpword:
            self.pword = newpword
            print("Password changed successfully")
        else:
            print("Invalid account number or password")
        
        
    def display(self, accnum, pword):
        if self.accnum == accnum and self.pword == pword:
            print(f"Displaying account details for {self.name} ......")
            time.sleep(1)  # Adding a delay of 1 second
            print(f"Account name: {self.name}")
            print(f"Account number: {self.accnum}")
            print(f"Account balance: {self.balance}")
        
        else:
            print("Invalid account number or password")

users = {}
while True:
    print("Welcome to the Banking System")
    time.sleep(1)
    print("Enter 1 to create an account")
    print("Enter 2 to display account details")
    print("Enter 3 to deposit money")
    print("Enter 4 to withdraw money")
    print("Enter 5 to change password")
    print("Enter 0 to exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        name = input("Enter your name: ")
        accnum = input("Enter your account number: ")
        pword = input("Enter your password: ")
        while True:
            if accnum not in users.keys():
                users[accnum] = Account(name, accnum, pword)
                print("Account created successfully")
                break
            else:
                print("Account already exists")
                accnum = input("Enter a different account number: ")
            
    elif choice==2:
        accnum = input("Enter your account number: ")
        pword = input("Enter your password: ")
        if accnum in users.keys():
            users[accnum].display(accnum, pword)
        else:
            print("Account not found")
    elif choice ==3:
        accnum = input("Enter your account number: ")
        pword = input("Enter your password: ")
        if accnum in users.keys():
            balance = float(input("Enter the amount to deposit: "))
            users[accnum].deposit(balance, accnum)
        else:
            print("Account not found")
    elif choice==4:
        accnum = input("Enter your account number: ")
        pword = input("Enter your password: ")
        if accnum in users.keys():
            balance = float(input("Enter the amount to withdraw: "))
            users[accnum].withdraw(balance, accnum, pword)
        else:
            print("Account not found")
    elif choice==5:
        accnum = input("Enter your account number: ")
        pword = input("Enter your password: ")
        if accnum in users.keys():
            oldpword = input("Enter your old password: ")
            newpword = input("Enter your new password: ")
            users[accnum].changepassword(oldpword, newpword, accnum)
        else:
            print("Account not found")
    elif choice==0:
        print("Exiting the banking system")
        break
    else:
        print("Invalid choice, please try again")
    