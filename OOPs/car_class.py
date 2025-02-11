class Car :
    def __init__(self , color , mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage} kms"
    def __str__(self):
        return f"The {self.color} car has {self.mileage} kms"


car1 = Car("Blue" , 2000)
car2 = Car("Red" , 5000)
print(car1)
print(car2)
print(car1.description())
print(car2.description())

print("Car")


class ElectricCar(Car):
    def __init__(self, color, mileage, battery_capacity):
        super().__init__(color, mileage)
        self.battery_capacity = battery_capacity
    
    def description(self):
        return f"The {self.color} electric car has {self.mileage} kms and {self.battery_capacity}kWh battery"

class SportsCar(Car):
    def __init__(self, color, mileage, top_speed):
        super().__init__(color, mileage) 
        self.top_speed = top_speed
    
    def description(self):
        return f"The {self.color} sports car has {self.mileage} kms and can reach {self.top_speed}km/h"

class Truck(Car):
    def __init__(self, color, mileage, cargo_capacity):
        super().__init__(color, mileage)
        self.cargo_capacity = cargo_capacity
    
    def description(self):
        return f"The {self.color} truck has {self.mileage} kms and can carry {self.cargo_capacity}kg"

# Create instances of new classes
tesla = ElectricCar("White", 1000, 75)
ferrari = SportsCar("Red", 500, 320) 
volvo = Truck("Black", 50000, 5000)

print("\nNew vehicles:")
print(tesla.description())
print(ferrari.description())
print(volvo.description())
