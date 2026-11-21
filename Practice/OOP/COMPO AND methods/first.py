class Library:

    def __init__(self, name):
        self.name = name

    def library_info(self):
        print(f"The Library's name is: {self.name}")


class Book(Library):

    def __init__(self, name, title, author):
        super().__init__(name)

        self.title = title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status != "Borrowed":
            self.status = "Borrowed"
            return True

        else:
            return False

    def show_info(self):
        print(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Status: {self.status}"
        )


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


book1 = Book(
    "PSHS Library",
    "Noli Me Tangere",
    "Jose Rizal"
)

student1 = Student("Drei")

book1.library_info()

student1.borrow_book(book1)

book1.show_info()

student1.borrow_book(book1)