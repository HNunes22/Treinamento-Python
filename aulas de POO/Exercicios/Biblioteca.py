# Classes

class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.available = "Available"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
                print(f"Tittle: {book.title}\nAuthor: {book.author}\nYear: {book.year}\nPages: {book.pages}\nAvailable: {book.available}\n")

    def book_loan(self, tittle):
        for book in self.books:
            if book.title == tittle:
                book.available = "Unavailable"
                return
        print("Not found.")


# Create the Books

book1 = Book("The Flute", "Jorgin Pietro", 1999, 67)
book2 = Book("Monopoly", "Gregory de Sá", 1977, 88)
book3 = Book("La Plause", "Faustine Merentiel", 2001, 92)

# Add Books in Library

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Method list from Library
library.book_loan("The Flute")
library.list_books()

