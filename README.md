File: bank.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

File: main.py
from bank import BankAccount

def main():
    account = BankAccount("Alice", 100)
    print(account)
    account.deposit(50)
    account.withdraw(30)
    print(account)

if __name__ == "__main__":
    main()

File: README.md

# Simple Bank Account Class

This is a basic Python project that demonstrates object-oriented programming (OOP) by implementing a `BankAccount` class. The class allows for creating accounts, depositing money, withdrawing money, and checking the account balance.

---

## Features

The `BankAccount` class supports the following operations:

* **Create Account:** Initialize a new account with an owner's name and an optional starting balance (defaults to 0).
* **Deposit:** Add a positive amount to the account balance.
* **Withdraw:** Subtract an amount from the balance. This action is only successful if the amount is positive and does not exceed the current balance.
* **Check Balance:** Print the account owner and current balance using a human-readable string representation.

---

## Files

* **`bank.py`**: Contains the `BankAccount` class definition, including its attributes (`owner`, `balance`) and methods (`deposit`, `withdraw`, `__str__`).
* **`main.py`**: A simple script that demonstrates how to import, create, and use an instance of the `BankAccount` class.

---

## Requirements

* Python 3.x

---

##  How to Use

To run the demonstration script, execute `main.py` from your terminal:

```bash
python main.py
