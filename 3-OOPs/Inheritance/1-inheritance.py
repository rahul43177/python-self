#Parent Class 
class Person:
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        return f"{self.firstname} {self.lastname}"


first_person  = Person("Rahul" , "Mishra")
second_person = Person("Muskan" , "Acharya")

print(first_person.print_name())
print(second_person.print_name())

# Child Class

class Student(Person):
    def __init__(self, fname , lname , year):
       super().__init__(fname , lname)
       self.graduation_year = year

    def print_student(self):
        return f"{self.firstname} {self.lastname}"
    
    def welcome(self):
        return f"Hi {self.firstname} , How are you!! , You are going to pass out from college on {self.graduation_year}"


x = Student("Anshul" , "Kumar" , 2022)
print(x.print_name())
print(x.welcome())