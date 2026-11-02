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

from bank import BankAccount

def main():
    account = BankAccount("Alice", 100)
    print(account)
    account.deposit(50)
    account.withdraw(30)
    print(account)

if __name__ == "__main__":
    main()
