class studentrecord:
    def __init__(self,name):
        self.name = name
        self._marks=[]
        self.__grade= None
#    
#     @property
#     def grade (self):
#         return self.__grade
    
#     @grade.setter
#     def set_grade(self,newgrade):
#         self.__grade= newgrade
# 

    def addmark(self, *mark):
        m = list(mark)
        self._marks = self._marks + m
        print("Marks added successfully")
        
        
    def _calculateevg(self):
        total = sum (self._marks)
        n = len(self._marks)
        return total/n
        
    
    def __assigngrade(self,avg):
        
        if avg >= 80:
            self.__grade = "A"
        elif avg >= 60:
            self.__grade = "B"
        elif avg >= 40:
            self.__grade = "C"
        else:
            self.__grade = "F"
        
        
        
    def finalize(self):
        avg = self._calculateevg()
        self.__assigngrade(avg)
        
    def getreport(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self._marks}")
        print(f"Average: {self._calculateevg()}")
        print(f"Grade: {self.__grade}")
        print("Report generated successfully.")
        return self.__grade
        

a = studentrecord("ram")
a.addmark(10, 20, 30, 40)
a.finalize()
a.getreport()


    