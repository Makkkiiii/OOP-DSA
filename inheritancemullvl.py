# Multi Level Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def showinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def eating(self):
        print(f"{self.name} is eating.")
        
        
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
        
    def showinfo(self):
        super().showinfo()
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")
        
    def working(self):
        print(f"{self.name} is working.")
        
class Lecturer(Employee):
    def __init__(self, name, age, emp_id, salary, subject):
        super().__init__(name, age, emp_id, salary)
        self.subject = subject
        
    def showinfo(self):
        super().showinfo()
        print(f"Subject: {self.subject}")
        
    def teaching(self):
        print(f"{self.name} is teaching {self.subject}.")
        
# b = Employee("Sumit", 30, 101, 50000)
# b.showinfo()

a = Lecturer("Sumit", 35, 102, 60000, "Business")
a.showinfo()