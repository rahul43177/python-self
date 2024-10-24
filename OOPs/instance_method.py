"""
Instance methods are functions that you define inside a class and can only call on an instance of that class. Just like .__init__(), an instance method always takes self as its first parameter.
"""

class Cat:
    color = "Brown"
    def __init__(self , name , age , speaks):
        self.name = name
        self.age = age
        self.speaks = speaks
    def description(self):
        return f"The name of the cat is {self.name} and {self.name} is {self.age} years old!"
    
    def speak(self):
        return f"{self.name} speaks {self.speaks}"
    def __str__(self):
        return f"{self.name} is {self.age} years old!"

cat1 = Cat("Billa" , 2 , "Meow")
print(cat1.description())
print(cat1.speak())
print(cat1)