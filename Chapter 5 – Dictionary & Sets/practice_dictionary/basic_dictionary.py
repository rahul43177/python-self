""" 
Basic Dictionary Operations:

- Create a dictionary named student with keys: name, age, and courses. Assign appropriate values to these keys.
- Add a new key grade with the value A to the student dictionary.
- Update the age key to a new value.
- Remove the courses key from the dictionary.
- Print all the keys and values in the dictionary.
"""

student = {
    "name" : "Rahul Mishra" , 
    "age" : 23 , 
    "courses" : ["Python Programming" , "Data Structures and Algorithms"]
}

student["grade"] = "A"

print(student)
student["age"] = 24
print(student)

del student["courses"] 
print(student)


