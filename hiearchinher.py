# Hierarchical Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def showinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def eating(self):
        print(f"{self.name} is eating.")
        
        
class Student(Person):
    def __init__(self, name, age, major,gpa):
        super().__init__(name, age)
        self.major = major
        self.gpa = gpa
        
    def showinfo(self):
        super().showinfo()
        print(f"Major: {self.major}, GPA: {self.gpa}")
        
    def learning(self):
        print(f"{self.name} is Learning {self.course}.")
        
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def showinfo(self):
        super().showinfo()
        print(f"Subject: {self.subject}")
        
    def teaching(self):
        print(f"{self.name} is teaching {self.subject}.")

# Example usage
student = Student(name="Shyam", age=20, major="Computer Science", gpa=3.8)
teacher = Teacher(name="Sumit", age=45, subject="Mathematics")

print("Student Details:")
student.showinfo()
print("\nTeacher Details:")
teacher.showinfo()
