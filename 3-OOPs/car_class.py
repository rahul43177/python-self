class Employee : 
    def __init__(self , name ,age , salary , gender) :
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    def description(self):
        gender = self.gender.lower() 
        statement = ""
        if gender == "male" :
            statement = "he"
        else :
            statement = "she"
        
        return f"{self.name} is {self.age} years old , and {statement} is earning {self.salary}" 
    
    def __str__(self):
        return (f"The class for Employees")



rahul = Employee("Rahul Mishra" , 24 , 700000 , "Male")
muskan = Employee("Muskan Acharya" , 24 , 800000 , "Female")


print(rahul.description())
print(muskan.description())
