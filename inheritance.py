class Person:
    #citizen  = "Nepali"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def eating (self):
        print(f"{self.name} is eating.")
        
    
    def display(self):
        print(f"Name is {self.name} and age is {self.age}.")
        
class Student(Person):
    def __init__(self,name,age,major):  
         
        # self.name = name
        # self.age = age
        
        super().__init__(name,age)
        self.major = major
        
    #college = "Coventry"
    
    def show (self):
        
       # print(f"I am studying at {self.college}")
       
       print(f"My name is {self.name}, I am {self.age} years old and I am studying {self.major}.")
       
       def eating (self):
           print ("Student is eating.")
            
a =  Student("Ram",16,"Hacking")
# print(a.name, a.age, a.major)
a.show()
a.eating()