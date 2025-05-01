class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Example usage
account = BankAccount("Alice", 100)
print(account.get_balance())
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))
