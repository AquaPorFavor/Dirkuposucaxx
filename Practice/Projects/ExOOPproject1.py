from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def __init__ (self, amount):
        self.amount = amount

    def pay(self, amount):
        print(f"Paid ₱{amount} using cash")


class CardPayment(Payment):
    def __init__ (self, amount):
        self.amount = amount

    def pay(self, amount):
        print(f"Paid ₱{amount} using card")


class GCashPayment(Payment):
    def __init__ (self, amount):
        self.amount = amount

    def pay(self, amount):
        print(f"Paid ₱{amount} using GCash")

class Customer:

    def __init__(self, name):
        self.name = name

    def make_payment(self, payment, amount):
        print(f"{self.name} is making a payment...")
        payment.pay(amount)


customer = Customer("Drei")

cash = CashPayment(600)
card = CardPayment(700)
gcash = GCashPayment(800)

customer.make_payment(cash, 500)
customer.make_payment(card, 1000)
customer.make_payment(gcash, 750)

