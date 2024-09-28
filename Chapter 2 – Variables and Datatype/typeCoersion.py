
# This program demonstrates implicit and explicit type coercion in Python.

# Define an integer variable
intNumber = 12

# Define a float variable
floatNumber = 23.23

# Implicit type coercion: Adding an integer and a float results in a float
newDataType = intNumber + floatNumber

# Print the type of the newDataType variable
print(type(newDataType))

# Explicit type coercion: Converting the float to an integer using the int() function
explicitTypeCoercion = int(floatNumber)

# Print the type of the explicitTypeCoercion variable
print(type(explicitTypeCoercion))

#explicit type coersion 
x = "123"
y = int(x)  # Convert string to int
print(y)    # Output: 123

a = 3.14
b = str(a)  # Convert float to string
print(b)    # Output: "3.14"


