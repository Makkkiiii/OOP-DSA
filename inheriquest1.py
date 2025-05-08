class User :
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
        
    def disuserinfo(self):
        print(f"Name: {self.name}, Email: {self.email}")
        
class Member(User):
    def __init__(self, name , email, memberid) :
        super().__init__(name, email)
        self.memberid = memberid
        self.__borrowed_books = []
        
    def borrow_book(self):
        book = input("Enter the name of the book you want to borrow: ")
        if len(self.__borrowed_books) >= 5:
            print("You cannot borrow more than 5 books at a time.")
        else:
            self.__borrowed_books.append(book)
            print(f"You have borrowed '{book}'.")
            
    def returnbook(self):
        book = input("Enter the name of the book you want to return: ")
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            print(f"You have returned '{book}'.")
        else:
            print(f"You cannot return '{book}'.")
            
    def display(self):
        print(f"Member ID: {self.memberid}")
        print(f"Borrowed Books: {', '.join(self.__borrowed_books) if self.__borrowed_books else 'No books borrowed'}")
        
class Librarian(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id = employee_id  

    def add_book(self, library, book):
        library._books.append(book)
        print(f"{book} added to the library.")

    def remove_book(self, library, book):
        if book in library._books:
            library._books.remove(book)
            print(f"{book} removed from the library.")
        else:
            print(f"{book} is not available in the library.")


class Library:
    def __init__(self):
        self._books = []  

    def display_books(self):
        print(f"Available Books: {', '.join(self._books) if self._books else 'No books available'}")
        
        
library = Library()
librarian = Librarian("Ram", "ram@example.com", "L001")
member = Member("Shyam", "shyam@example.com", "M001")

        
librarian.add_book(library, "Python Programming")
librarian.add_book(library, "Data Structures")
librarian.add_book(library, "Algorithms")

        
library.display_books()

member.borrow_book()
member.display()

member.returnbook()
member.display()

librarian.remove_book(library, "Data Structures")
library.display_books()
