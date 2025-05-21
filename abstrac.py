from abc import ABC, abstractmethod

class Interest(ABC):
    @abstractmethod
    def calculateinterest(self):
        pass
    
class SI(Interest):
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
    
    def calculateinterest(self):
        i = self.principal * self.rate * self.time / 100
        print(f"Simple Interest is {i}")
        
class CI(Interest):
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time
    
    def calculateinterest(self):
        i = self.principal * (1 + self.rate / 100) ** self.time - self.principal
        print(f"Compound Interest is {i}")
        
h1 = SI(1000, 5, 2)
d1 = CI(1000, 5, 2)
for interest in [h1, d1]:
    interest.calculateinterest()
    