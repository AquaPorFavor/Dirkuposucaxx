class InvalidBalanceError(Exception):
    pass


class BankAcc:

    def __init__(self, accnum, balance):
        self.__accnum = accnum
        self.__balance = float(balance)

    @property
    def accnum(self):
        return self.__accnum

    @accnum.setter
    def accnum(self, new_accnum):
        if len(str(new_accnum)) == 5:
            self.__accnum = new_accnum
        else:
            raise ValueError("Account number must be 5 digits!")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self.__balance = float(new_balance)
        else:
            raise InvalidBalanceError("Balance must be bigger than zero or not negative!")

a1 = BankAcc(12345, 1000)


print(a1.accnum)
print(a1.balance)

a1.accnum = 54321
a1.balance = 2000


print(a1.accnum)
print(a1.balance)


try:
    a1.accnum = -100
except ValueError as error:
    print(error)

try:
    a1.balance = -500

except InvalidBalanceError as error:
    print(f"Error: {error}")
