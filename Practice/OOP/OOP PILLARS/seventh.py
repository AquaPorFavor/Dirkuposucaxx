class CashPayment:
    def pay(self, amount):
        return f"Paid {amount} in cash"


class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} using a card"


class GCashPayment:
    def pay(self, amount):
        return f"Paid {amount} using GCash"


payments = [CashPayment(), CardPayment(), GCashPayment()]

for p in payments:
    print(p.pay(500))