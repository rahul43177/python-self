name = "Rahul"
fruits = ["Banana" , "Apple"  , "Watermelon"]
print(fruits)
if name == "Rahul":
    print(f"The name is -> {name}")
elif name != "Rahul":
    print(f"Although the name is not rahul , but the name is -> {name}")

if "Apple" in fruits:
    print("The apple is there in the house")
else : 
    print("we need to shop some apples")

if "banana" not in fruits : 
    fruits.append("banana")
    print("The bananas have been added in the fruit list")
else :
    print("The banana was already present")
    
print(f"The fruits in the house are -> {fruits}")


persons = {
    "person1" :{
        "name" : "Rahul" , 
        "age" : 23 , 
        "gender" : "Male" , 
        "email" : "rahul@gmail.com"
    } , 
    "person2" :{
        "name" : "Anshul" , 
        "age" : 25 , 
        "gender" : "Female" , 
        "email" : "anshul@gmail.com"
    },
    "person3" :{
        "name" : "Vikram" , 
        "age" : 30 , 
        "gender" : "Male" , 
        "email" : "vikram@gmail.com"
    },
    "person4" :{
        "name" : "Ayush" , 
        "age" : 28 , 
        "gender" : "Female" , 
        "email" : "ayush@gmail.com"
    }
}


for person in persons :
    if persons[person]["name"] == "Rahul" :
        persons[person]["age"] += 1 
        print("Increased rahul's age by 1 , as birthday is approaching")
        break;
    else :
        print("Could not find rahul in the person data")
        

print(f"The persons -> {persons}")


#Ternary operator 
# <expression_if_true> if <condition> else <expression_if_false>

a = 10 
b = 20 

print("A is greater than B") if a > b else print("The B is greater than A")

def calulcateIsValidVoter(age):
    return True if age >=18 else False

age = int(input("Please enter your age : "))
isValid = calulcateIsValidVoter(age)
print("The person is eligible") if isValid else print("The person is ineligible")
