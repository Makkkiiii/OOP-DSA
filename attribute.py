class Student:
    college = "Softwarica"
    Nationality = "Nepali"
    def __init__(self, name, major):
        self.name = name
        self.major = major
        
    @classmethod
    def change_nationality(cls,n):
        cls.Nationality = n
    
    
    @classmethod
    def alt_cons(cls,name,major):
        return cls(name,major)
    
    @staticmethod
    def average(*marks):
        total = sum (marks)
        n = len(marks)
        avg=total/n
        print(f"Average of {n} subjects is {avg}")
        
        
    
    def display (self):
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        
        
a = Student("John", "Computer Science")
b = Student("Jane", "Information Technology")
c = Student.alt_cons("Ram", "Computing")
print (c.name)
Student.average(56,67)
Student.average(45,78,64)