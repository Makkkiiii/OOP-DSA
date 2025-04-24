class BankAccount:
    def __init__(self, account_holder, account_type, initial_balance=0):
        self.account_holder = account_holder  
        self._account_type = account_type  
        self.__balance = initial_balance  

    
    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        print(f"Current Balance: ${self.__balance:.2f}")

    
    def _update_account_type(self, new_type):
        self._account_type = new_type
        print(f"Account type updated to {new_type}")

   
    def __validate_transaction(self, amount):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

    
    def deposit(self, amount):
        self.__validate_transaction(amount)
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    
    def withdraw(self, amount):
        self.__validate_transaction(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

   
    @property
    def balance(self):
        return self.__balance

    
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = new_balance



account = BankAccount("John Doe", "Savings", 1000)
account.display_account_details()
account.deposit(500)
account.withdraw(300)
account._update_account_type("Checking")
account.display_account_details()