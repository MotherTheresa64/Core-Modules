# Final challenge: ATM withdrawal simulation

account_balance = 1500

try:
    amount = float(input("Enter amount to withdraw: "))

    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if amount > account_balance:
        raise ValueError("Insufficient funds.")

    account_balance -= amount
    print(f"Withdrawal successful. ${amount} withdrawn.")
except ValueError as e:
    print(f"Transaction error: {e}")
finally:
    print(f"Remaining balance: ${account_balance}")
