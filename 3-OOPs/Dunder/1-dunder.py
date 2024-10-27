class Employee:
    def __init__(self , name):
        self.name = name 
    
    def __length__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    
    
e = Employee("Rahul")
print(e.__length__())

