class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"{self.name} is {self.age} years old"
    
    def update_age(self , new_age):
        self.age = new_age
    
    def __repr__(self):
        return f"{self.name} is {self.age} years old"
    

rahul = Student("Rahul Mishra" , 24)

print(rahul)