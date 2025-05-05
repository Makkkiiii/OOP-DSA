# Base class
class LibraryMember:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def borrow_book(self, book_title):
        print(f"{self.name} (ID: {self.membership_id}) borrowed the book: {book_title}")

    def return_book(self, book_title):
        print(f"{self.name} (ID: {self.membership_id}) returned the book: {book_title}")

# Derived class
class StudentMember(LibraryMember):
    def __init__(self, name, membership_id, student_id):
        super().__init__(name, membership_id)
        self.student_id = student_id

    def borrow_book(self, book_title):
        print(f"Student {self.name} (Student ID: {self.student_id}) is borrowing a book.")
        super().borrow_book(book_title)

    def access_study_room(self):
        print(f"Student {self.name} (Student ID: {self.student_id}) accessed the study room.")

member = LibraryMember("Ram", "RM001")
member.borrow_book("Python Programming")
member.return_book("Python Programming")

print()


student = StudentMember("Shyam", "SM001", "ST123")
student.borrow_book("Data Structures")
student.return_book("Data Structures")
student.access_study_room()