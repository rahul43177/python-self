# Dictionary Methods
""" 
Here are some useful dictionary methods:
keys(): Returns a view object that displays a list of all the keys in the dictionary.
values(): Returns a view object that displays a list of all the values in the dictionary.
items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
"""

person = {
    "name" : "Rahul Mishraa" , 
    "age" : 23 , 
    "gender" : "Male" , 
    "email" : "rahul@gmail.com" 
}

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print(keys)   # Output: dict_keys(['name', 'age'])
print(values) # Output: dict_values(['Alice', 31])
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 31)])

# Iterating through keys
for key in person:
    print(key, person[key])

# Iterating through key-value pairs
for key, value in person.items():
    print(key, value)
    
    
