# Base class
class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance):
        self.account_holder_name = account_holder_name
        self._balance = initial_balance 
        self.__account_number = account_number 

    def deposit(self, amount):
        self._balance += amount
        print(f"{self.account_holder_name} deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Insufficient balance for {self.account_holder_name}.")
        else:
            self._balance -= amount
            print(f"{self.account_holder_name} withdrew {amount}. New balance: {self._balance}")

    def _generate_statement(self):
        print(f"Account Statement for {self.account_holder_name}: Balance = {self._balance}")

# Derived class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, initial_balance, interest_rate):
        super().__init__(account_holder_name, account_number, initial_balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = amount * self.interest_rate / 100
        total_amount = amount + interest
        print(f"Adding interest of {interest} to the deposit.")
        super().deposit(total_amount)

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Interest Rate: {self.interest_rate}%")
        self._generate_statement()


account = BankAccount("Hari", "HA001", 1000)
account.deposit(500)
account.withdraw(300)

print() 

savings = SavingsAccount("Bari", "HA001", 2000, 5)
savings.deposit(1000) 
savings.withdraw(500)
savings.display_account_info()