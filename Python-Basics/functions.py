
def greeting(name):
    """Greets the user

    Args:
        name (string): Name of the user
    """
    return f"Hello , How are you {name} ?"
name = "Rahul"
print(greeting(name))

print(greeting(name = "Muskan")) #Keyword arguements -> passing with that particular keyword in the parameter
print(greeting("Muskan")) #positional arguements -> takes the arguement at that particular position

#DEFAULT PARAMETER
def greet(name , message = "How are you ?"): #default parameter , if nothing is given in the message , it will take "How are you" by default
    """Greet the user

    Args:
        name (str): _description_
        message (str, optional): _description_. Defaults to "How are you ?".
    """
    return f"hi {name} , {message}"

print(greet(message = "Hi Whatsapp" , name = "Rahul Mishra"))
print(greet(name = "Rahul Mishra")) #default parameter will be taken


# Variable-Length Arguments
def print_numbers(*args):
    """Print all the numbers in the parameter"""
    try:
        for number in args :
            if type(number) != int:
                raise ValueError(f"{number} is not a valid number")    
            else :
                print(number)
    except ValueError as e:
        print("error" ,  e)
        
    
print_numbers(1,2,3,4,5,6,7,8,9,"10")
    
# Lambda
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

add = lambda num1 , num2 : num1+num2
print(add(10,20))

greeting = lambda name , message = "How are you ? " : f"Hi {name} , {message}"

print(greeting(name = "Rahul Mishra" , message = "Whatsapp ?"))

greeting_to_user = lambda name ,  message = "Hello sir" : f"{name} , {message}"

print(greeting_to_user("Rahul" , "sab changa si ?"))


#SCOPE 

x = "global"

def function_scope():
    x = "Local"
    print(x) #local
    
function_scope()

def new_function_scope():
    global x
    x = "global to local"
    print(x)

new_function_scope()
print(x)