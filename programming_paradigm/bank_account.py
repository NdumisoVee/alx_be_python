class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        print(f"Deposited: ${amount}")
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
