class Person:
    citizen  = "Nepali"
    
    def display(self):
        print(f"We are {self.citizen}")
        
class Student(Person):
    pass
    
a =  Student()
print(a.citizen) 
a.display()