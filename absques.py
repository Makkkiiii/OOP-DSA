from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def add_book(self, book_name: str):
        pass

    @abstractmethod
    def borrow_book(self, book_name: str):
        pass

    @abstractmethod
    def return_book(self, book_name: str):
        pass

    @abstractmethod
    def display_books(self):
        pass

class PublicLibrary(Library):
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, book_name: str):
        self.available_books.append(book_name)
        print(f'"{book_name}" added to the library.')

    def borrow_book(self, book_name: str):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f'You have borrowed "{book_name}".')
        else:
            print(f'Sorry, "{book_name}" is not available for borrowing.')

    def return_book(self, book_name: str):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.available_books.append(book_name)
            print(f'You have returned "{book_name}".')
        else:
            print(f'"{book_name}" was not borrowed from this library.')

    def display_books(self):
        if self.available_books:
            print("Available books in the library:")
            for book in self.available_books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")

if __name__ == "__main__":
    library = PublicLibrary()
    # Add initial books
    library.add_book("Python 101")
    library.add_book("Data Structures")
    library.add_book("Machine Learning")

    while True:
        print("\nLibrary Menu:")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book = input("Enter the name of the book to borrow: ")
            library.borrow_book(book)
        elif choice == "3":
            book = input("Enter the name of the book to return: ")
            library.return_book(book)
        elif choice == "4":
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")