class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, newbook):
        print(f"{newbook.title} has been added")
        self.books.append(newbook)

    def show_book(self):
        return self.books
    
class Book:
    def __init__(self, title, author):
        self.title =title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status != "Borrowed":
            self.status = "Borrowed"
            return True

        else:
            return False

    def returnb(self):
        self.status = "Available"
        print(f"{self.title} has been returned")

    def show_info(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nStatus {self.status}")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_book = book
            print(f"Student {self.name} has borrowed {book.title}")

        else:
            print(f"Book {book.title} is already borrowed!")

    def return_book(self):
        if self.borrowed_book is not None:
            self.borrowed_book.returnb()
            self.borrowed_book = None


book1 = Book("Harry Potter", "JK. Rowling")
library = Library("PSHS Library")
student1 = Student("Drei")

library.add_books(book1)

student1.borrow_book(book1)

student1.return_book()

library.show_book()
        

    