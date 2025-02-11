# Creating a tuple
fruits = ('apple', 'banana', 'cherry')
print("Tuple:", fruits)

# Creating a tuple with a single element
single_element_tuple = ('apple',)  # Note the comma
print("Single element tuple:", single_element_tuple)

# Tuple without parentheses
numbers = 1, 2, 3
print("Tuple without parentheses:", numbers)

# Unpacking a tuple
a, b, c = fruits
print("Unpacked:", a, b, c)

# Attempting to modify a tuple (will raise an error)
try:
    fruits[0] = 'blueberry'
except TypeError as e:
    print("Error:", e) #Error: 'tuple' object does not support item assignment
    
# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))


