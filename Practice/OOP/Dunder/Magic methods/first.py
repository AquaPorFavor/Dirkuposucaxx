'''
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

    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

        Book.total_books +=1

    def borrow(self):
        if self.status != "Borrowed":
            self.status = "Borrowed"
            return True

        else:
            return False

    def returnb(self):
        self.status = "Available"
        print(f"{self.title} has been returned")

    def __str__(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nStatus {self.status}")

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    


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
book2 = Book("Harry Potter", "JK. Rowling")
library = Library("PSHS Library")
student1 = Student("Drei")

library.add_books(book1)

student1.borrow_book(book1)

print(book1)

print(book1 == book2)



student1.return_book()

library.show_book()
         
'''

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, newbook):
        print(f"{newbook.title} has been added")
        self.books.append(newbook)

    def show_book(self):
        return self.books

    def __len__(self):
        return len(self.books)


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.__title = title
        self.author = author
        self.status = "Available"
        Book.total_books += 1

    def borrow(self):
        if self.status != "Borrowed":
            self.status = "Borrowed"
            return True
        return False

    def returnb(self):
        self.status = "Available"
        print(f"{self.title} has been returned")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self.__title = new_title

    @classmethod
    def show_total_books(cls):
        print(f"Total books: {cls.total_books}")

    @staticmethod
    def valid_title(title):
        return len(title) > 0

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    
    
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


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Harry Potter", "J.K. Rowling")

library = Library("PSHS Library")

student1 = Student("Drei")

library.add_books(book1)

student1.borrow_book(book1)

student1.return_book()

library.show_book()

Book.show_total_books()

print(book1)
print(book1 == book2)
print(len(library))
print(book1.title)
book1.title = "Chamber of Secrets"
print(book1.title)
print(f"The book is valid: {Book.valid_title(book1.title)}")