class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

        else:
            print("positive amount only")

    def withdraw(self, amount):

        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount

            else:
                print("insuffficient balance")

        else:
            print("amount must be negative")

    def curr_balance(self):
        print(f"current balance is {self.balance}")


account1 = BankAccount("Safa", 1000)
account1.deposit(2000)

account1.withdraw(1000)

account1.curr_balance()
