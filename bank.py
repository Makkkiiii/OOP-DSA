class BankAccount:
    def __init__(self, account_holder, account_type, initial_balance=0):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = initial_balance

    def deposit(self, amount):
        if self.__validate_transaction(amount):
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit failed. Amount must be positive.")

    def withdraw(self, amount):
        if not self.__validate_transaction(amount):
            print("Withdrawal failed. Amount must be positive.")
        elif amount > self.__balance:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def _update_account_type(self, new_type):
        self._account_type = new_type
        print(f"Account type updated to {new_type}")

    def __validate_transaction(self, amount):
        return amount > 0

    def display_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        print(f"Balance: ${self.__balance:.2f}")
        print("Account details displayed successfully.")
        return self.__balance



acc = BankAccount("John Doe", "Savings", 1000)
acc.display_account()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000) 
acc.deposit(-100)  
acc._update_account_type("Checking")
acc.display_account()
