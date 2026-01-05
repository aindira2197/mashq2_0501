class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so'm qo‘shildi")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi")
        else:
            print("Hisobda yetarli mablag‘ yo‘q")

    def show_balance(self):
        print(f"Balans: {self.balance} so'm")



acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
