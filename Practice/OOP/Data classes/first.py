from dataclasses import dataclass

@dataclass
class Book:
    
    title: str
    author: str
    status: str = "Available"
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}"

book1 = Book("Chamber of Secrets", "Joke lang")

print(book1)