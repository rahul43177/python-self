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