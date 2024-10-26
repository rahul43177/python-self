class Dog:
    def __init__(self , name , age , breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self , sound):
        return f"{self.name} speaks {sound}"
    
    def __str__(self) :
        return f"The dog name is {self.name} and it is {self.age} years old and the Breed is {self.breed}"

    

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(miles)
print(buddy.speak("Meow"))
