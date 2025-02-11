class Dog:
    spicies = "Bull Dog"
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def description(self) :
        return f"{self.name} is {self.age} years old"
    
    def speak(self , sound):
        return f"{self.name} says {sound}"
    
    
a = Dog("Cutie" , 3)
print(a.spicies)


miles = Dog("Miles" , 4)
description = miles.description()
print(description)


speak = miles.speak("Woof woof")
print(speak)

class Parent:
    hair_color = "Brown"

class Children(Parent):
    hair_color = "Purple"
    
    
color = Children.hair_color
print(color)



# inheritance.py

class Parenting:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

