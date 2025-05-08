# Hybrid Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def showinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def eating(self):
        print(f"{self.name} is eating.")

class Student(Person):
    def __init__(self, name, age, major, gpa):
        Person.__init__(self, name, age)
        self.major = major
        self.gpa = gpa
        
    def showinfo(self):
        Person.showinfo(self)
        print(f"Major: {self.major}, GPA: {self.gpa}")
        
    def learning(self, course):
        print(f"{self.name} is learning {course}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject
        
    def showinfo(self):
        Person.showinfo(self)
        print(f"Subject: {self.subject}")
        
    def teaching(self):
        print(f"{self.name} is teaching {self.subject}.")

class TA(Student, Teacher):
    def __init__(self, name, age, major, gpa, subject):
        Person.__init__(self, name, age)
        self.major = major
        self.gpa = gpa
        self.subject = subject
        
    def showinfo(self):
        Person.showinfo(self)
        print(f"Major: {self.major}, GPA: {self.gpa}")
        print(f"Subject for TA: {self.subject}")


a = TA("Shyam", 20, "Computer Science", 3.8, "Python Programming")
a.showinfo()
