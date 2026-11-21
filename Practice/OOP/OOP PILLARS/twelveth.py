from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self._history = []

    # Encapsulation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._history.append(f"Withdrew {amount}")
            return True
        return False

    def get_balance(self):
        return self.__balance

    def show_history(self):
        return self._history

    # Abstraction
    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def account_type(self):
        pass

    # Shared summary
    def summary(self):
        return (
            f"{self.account_type()} | "
            f"Owner: {self.owner} | "
            f"Balance: {self.get_balance():.2f}"
        )


class SavingsAccount(Account):

    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        self.deposit(interest)
        return interest

    def account_type(self):
        return "Savings"


class CurrentAccount(Account):

    def calculate_interest(self):
        return 0

    def account_type(self):
        return "Current"


class LoanAccount(Account):

    def calculate_interest(self):
        interest = self.get_balance() * 0.10
        self.deposit(interest)
        return interest

    def account_type(self):
        return "Loan"


# Create accounts
accounts = [
    SavingsAccount("Aqua", 1000),
    CurrentAccount("Paulo", 500),
    LoanAccount("Luna", 2000)
]

# Transactions
accounts[0].deposit(200)
accounts[0].withdraw(150)

accounts[1].withdraw(100)

accounts[2].deposit(500)

# Interest
for acc in accounts:
    interest = acc.calculate_interest()
    print(f"Interest added to {acc.owner}: {interest:.2f}")

print("\n--- Account Summaries ---")

# Polymorphism
for acc in accounts:
    print(acc.summary())
    print("History:", acc.show_history())
    print()