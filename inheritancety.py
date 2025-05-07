#  Multiple Inheritance 

class Student :
    def __init__(self, sid, major):
        self.sid = sid 
        self.major = major
        
        
    def studying (self) : 
        print(f"Student with ID {self.sid} is studying {self.major}.")
        
class Teacher : 
    def __init__(self, sub, salary ):
        self.sub = sub 
        self.salary = salary
        
    def teaching (self) :
        print(f"Teacher is teaching {self.sub} with a salary of {self.salary}.")
        
class TA (Student, Teacher) : 
    def __init__(self, sid, major, sub, salary,hour):
        Student.__init__(self, sid, major)
        Teacher.__init__(self, sub, salary)
        self.hour = hour
        
    def info (self) :
        Student.studying(self)
        Teacher.teaching(self)
        print(f"TA with ID {self.sid} has {self.hour} hours of work.")
        
a = TA(123, "CS", "Python", 50000, 20)

a.info()