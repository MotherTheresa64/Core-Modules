class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Protected

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self._balance}"
        return "Insufficient funds."


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self._balance * rate
        self._balance += interest
        return f"Interest of ${interest:.2f} added. Balance: ${self._balance:.2f}"


class CheckingAccount(BankAccount):
    def deduct_fee(self, fee):
        self._balance -= fee
        return f"Fee of ${fee} deducted. Balance: ${self._balance}"


savings = SavingsAccount("Alice", 1000)
print(savings.deposit(500))
print(savings.add_interest(0.05))

checking = CheckingAccount("Bob", 500)
print(checking.withdraw(100))
print(checking.deduct_fee(20))
