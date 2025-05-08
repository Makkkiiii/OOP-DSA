class User:
    def __init__(self, name, email):
        self.name = name
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    def info(self):
        print(f"Username is {self.name} and email is {self._email}")


class Member(User):
    def __init__(self, name, email, memid):
        super().__init__(name, email)
        self.__memid = memid
        self.borrowed = []

    def borrow_book(self, library):
        book = input('Name of the book you want to borrow: ')
        if len(self.borrowed) < 5 and book in library.books:
            self.borrowed.append(book)
            library.books.remove(book)  # Remove the book from the library
            print("Book is borrowed")
        else:
            print("You can't borrow more than 5 books or the book is not available")

    def return_book(self, library):
        book = input("Name of the book you want to return: ")
        if book in self.borrowed:
            self.borrowed.remove(book)
            library.books.append(book)  # Add the book back to the library
            print("Book is returned")
        else:
            print("You can't return this book")

    def display(self):
        print(f"You have borrowed {self.borrowed} books")


class Librarian(User):
    def __init__(self, name, email, empid):
        super().__init__(name, email)
        self.__empid = empid

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Book '{book}' is added to the library")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"The book '{book}' is removed from the library")
        else:
            print("This book is not in the library")


class Library:
    def __init__(self):
        self.books = []

    def display_available_books(self):
        if self.books:
            print(f"Available books in library: {self.books}")
        else:
            print("No books available in the library.")


# Create a library instance
library = Library()

# Create a librarian instance
librarian = Librarian("Ram", "ram@gmail.com", 84570)

# Dictionary to hold members
members = {}

# Menu-driven interface
while True:
    print("\nMenu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Check available books")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Add a new member")  # Create a member instance
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book = input("Enter the name of the book to add to the library: ")
            librarian.add_book(library, book)

        elif choice == 2:
            book = input("Enter the name of the book to remove from the library: ")
            librarian.remove_book(library, book)

        elif choice == 3:
            library.display_available_books()

        elif choice == 4:
            memid = input("Enter your member ID: ")
            if memid in members:
                members[memid].borrow_book(library)
            else:
                print("Member not found.")

        elif choice == 5:
            memid = input("Enter your member ID: ")
            if memid in members:
                members[memid].return_book(library)
            else:
                print("Member not found.")

        elif choice == 6:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            memid = input("Enter your member ID: ")
            if memid not in members.keys():
                members[memid] = Member(name, email, memid)
                print(f"Member '{name}' added successfully.")
            else:
                print("Member ID already exists.")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")