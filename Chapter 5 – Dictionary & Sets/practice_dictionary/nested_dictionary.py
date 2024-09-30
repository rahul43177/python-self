""" 
Nested Dictionaries

- Create a dictionary named `classroom` where each key is a student's name and the value is another dictionary containing `age` and `grade`.
- Access and print the grade of a specific student.
- Add a new student to the `classroom` dictionary.
- Update the grade of an existing student.
"""

classroom = {
    "Rahul" : {
        "age" : 24 , 
        "grade" : "A"
    } , 
    "Anshul" : {
        "age" : 24 , 
        "grade" : "B"
    }
}

#printing the grade of Anshul
grade_of_anshul = classroom["Anshul"]["grade"]
print(grade_of_anshul)

#adding a new student
classroom["Muskan"] = {
    "age" : 24 , 
    "grade" : "A+"
}
print(classroom)
#update the grade of existing student
classroom["Anshul"]["grade"]= "A"
print(classroom)

