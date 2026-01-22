class Student :
    def __init__(self , name , year , enrolled , gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa

    def display_info(self):
        print(f"The student name : {self.name} and the GPA : {self.gpa}")

rahul = Student("Rahul Mishra"  , 2025 , True , 8.03)
rahul.display_info()

