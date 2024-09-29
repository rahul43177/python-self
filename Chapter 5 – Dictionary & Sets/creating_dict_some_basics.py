#creating a dictionary
person = {
    "name" : "Rahul" , 
    "age" : 23 , 
    "gender" : "Male"
}

print(person)

# Accessing Values
name_of_the_person = person["name"]
print(name_of_the_person)
age_of_the_person = person["age"]
print(age_of_the_person)
gender = person["gender"]
print(gender)

# Adding or Updating Items
#adding
print("the person before updation ->" , person)
person["email"] = "rahul@gmail.com"
print("added the email ->",person)
#updating 
person["age"] = 30
print("updated the age->",person)

# Removing Items -> removing a key - value pair 
#we have two methods -> del and pop
# Using del statement
del person["gender"]
# Using pop() method
email = person.pop("email")
print(f"The person object after deletion -> {person}")

