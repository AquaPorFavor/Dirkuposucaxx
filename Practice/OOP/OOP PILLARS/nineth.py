class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.__stock = stock   # private attribute

    # Encapsulation methods
    def add_stock(self, qty):
        self.__stock += qty

    def buy(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False

    def get_stock(self):
        return self.__stock

    def display(self):
        pass


class Book(Product):
    def display(self):
        return f"Book: {self.name} - PHP {self.price}"


class Phone(Product):
    def display(self):
        return f"Phone: {self.name} - PHP {self.price}"


class Shirt(Product):
    def display(self):
        return f"Shirt: {self.name} - PHP {self.price}"


# Create objects
b = Book("Harry Potter", 90, 10)
p = Phone("Nokia", 100, 5)
s = Shirt("Nike", 150, 20)

# Polymorphism
products = [b, p, s]

for item in products:
    print(item.display())
    print("Stock:", item.get_stock())
    print()

# Test encapsulation
b.buy(3)
print("After buying 3 books:", b.get_stock())