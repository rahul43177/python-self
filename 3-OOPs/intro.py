class Dog:
    spicies = "Pit Bull"
    def __init__(self , name , age):
        self.name = name
        self.age = age
    

dog1 = Dog("Moti" , 2)
dog2 = Dog("Cutie" , 3)


print(f"The name of the dog is {dog1.name}")
print(f"The name of the dog2 is {dog2.name}")
print(dog1.spicies)

dog1.spicies = "German Sephered"
dog2.age = 5
print(dog2.age)
print(dog1.spicies)