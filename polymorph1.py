# DUNDER

class Book:
    def __init__(self,name,page):
        self.name=name
        self.page=page
        
    def __add__(self,other): #MAGIC
        return self.page + other.page
    
    def __lt__(self,other):
        if self.page < other.page:
            return True
        else:
            return False
    
b1 = Book("Python", 200)
b2 = Book("Java", 300)
# print(b1+b2) 
print(b1 < b2) 
