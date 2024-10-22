#Position , name , age , level , salary
se1 = ["Software Engineer" , "Rahul Mishra" , 24 , "SE-1" , 700000]
se2 = ["Senior Software Engineer" , "Vishesh Singh Ujjain" , 29 , "SSE" , 2400000]

#class 
class SoftwareEngineer:
    #class attribute
    alias = "Magician"
    
    def __init__(self , name , age , level): #constructor
        #instance attribute
        self.name = name #it can be used in the entire class now 
        self.age = age
        self.level = level    

#instance of the class 
se1 = SoftwareEngineer("Rahul Mishra" , 24 , "SE")

print(se1.alias)


