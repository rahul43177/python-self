# Function to reverse a string
def reverse_string(input_string):
    reversed_string = ""
    # Using for loop to reverse the string
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Test the function
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)

