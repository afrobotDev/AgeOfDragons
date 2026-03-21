class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        books_to_keep = []
        for book_item in self.books:
            if book_item.title != book.title or book_item.author != book.author:
                books_to_keep.append(book_item)
        self.books = books_to_keep

    def search_books(self, search_string):
        book_match = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                book_match.append(book)
        return book_match
