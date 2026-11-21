class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def getbalance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)

print(acc.getbalance())  