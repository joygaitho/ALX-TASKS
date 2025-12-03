class Book:
    total_books = 0
    def __init__(self, name):
        self.name = name
        # Increment the class variable every time a new instance is created
        Book.total_books += 1 

    @classmethod
    def display_total_book(cls):
        """
        Class method to display the total number of book instances created.
        The 'cls' parameter refers to the class itself (Book).
        """
        print(f"Total number of books is: {cls.total_books}")

book1 = Book("home alone")
book2 = Book("home alone 2")

print("\n-- display count via Class")
Book.display_total_book()

print("\n-- display count via Object")
book2.display_total_book()