class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages}) pages"
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages})"

book1 = Book("1984", "George Orwell", 328)
print(str(book1))
print(repr(book1))