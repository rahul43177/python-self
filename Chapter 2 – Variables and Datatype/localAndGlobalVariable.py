x = "global"

def my_function():
    x = "local"
    print(x)  # Output: local

my_function()
print(x)  # Output: global

#we can also use global keyword to make the local variable as -> global

x = "global"

def new_function():
    global x
    x = "modified global"
    print(x)  # Output: modified global

new_function()
print(x)  # Output: modified global


NAME = "Rahul"

NAME = "mishra"
print(NAME)
NAME = "Rahul"  # Constant variable

print(NAME)  # Output: Rahul
