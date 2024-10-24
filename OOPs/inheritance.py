class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("Hindi")
    
    def description(self):
        return f"Child speaks -> {self.speaks}"
    
child = Child()
parent = Parent()
print(child.description())