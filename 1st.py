class car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand  
        self.gear = 0
        self.moving =  False
        
        
    def start(self):
        if self.moving == False:
            self.moving = True
            self.gear = 1
            print("Car started")
        else:
            print("Car is already moving")
            
            
    def changegear(self, new):
        if self.moving == True:
            self.gear =  new 
            print(f"Gear changed to {new}")
        else:
            print("Car is not moving")
            
            
    def display(self):
        print(f"Car color: {self.color}")
        print(f"Car brand: {self.brand}")
        print(f"Car gear: {self.gear}")
        print(f"Car moving: {self.moving}") 
        
car1 =  car("Red", "Toyota")
car1.start()
car1.changegear(3)

car1.display()