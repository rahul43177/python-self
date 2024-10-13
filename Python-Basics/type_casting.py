# Type Casting in Python

# Implicit Type Casting
# Python automatically converts one data type to another without any user intervention.
# This is known as implicit type casting.

# Example of Implicit Type Casting
num_int = 123   # int
num_float = 1.23  # float

# Adding integer and float
num_new = num_int + num_float

print("Data type of num_int:", type(num_int))
print("Data type of num_float:", type(num_float))
print("Value of num_new:", num_new)
print("Data type of num_new:", type(num_new))

# Explicit Type Casting
# The process where the user converts the data type of an object to the required data type.
# This is known as explicit type casting.

# Example of Explicit Type Casting
num_str = "456"  # str

# Converting string to integer
num_int = int(num_str)

print("Data type of num_str:", type(num_str))
print("Value of num_int:", num_int)
print("Data type of num_int:", type(num_int))

# Converting integer to float
num_float = float(num_int)

print("Value of num_float:", num_float)
print("Data type of num_float:", type(num_float))