class User :
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
        
    def disuserinfo(self):
        print(f"Name: {self.name}, Email: {self.email}")
        
class Member(User):
    def __init__(self, name , email, memberid) :
        super().__init__(name, email)
        self.memberid = memberid
        self.__borrewed_books = []