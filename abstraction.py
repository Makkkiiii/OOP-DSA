from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Human(Animal):
    def sound(self):
        print(f"Humans can speak")
    
class Dog(Animal):
    def sound(self):
        print(f"Dogs can't speak but bark")

h1=Human()
d1=Dog()
for animal in [h1,d1]:
    animal.sound()