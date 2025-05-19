class teacher:
    def eats(self):
        print("He is a teacher and he eats")
        
class student:
    def eats(self):
        print("He is a student and he eats")
        
        
def call_eats(a):
    a.eats()
    
b=teacher()
c=student()
call_eats(b)
call_eats(c)