# Exception Handling in Python

# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

# Basic syntax for exception handling in Python:
# try:
#     # Code that might raise an exception
# except SomeException as e:
#     # Code that runs if the exception occurs
# else:
#     # Code that runs if no exception occurs
# finally:
#     # Code that always runs, regardless of whether an exception occurred or not

# Example of handling a ZeroDivisionError exception

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
else:
    print("The division was successful.")
finally:
    print("This block always executes.")

# Example of handling multiple exceptions

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError occurred: {e}")
except TypeError as e:
    print(f"TypeError occurred: {e}")
else:
    print("The operation was successful.")
finally:
    print("This block always executes.")

# Example of raising an exception

try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print(f"A ValueError occurred: {e}")
finally:
    print("This block always executes.")
    
    


# Exception self
#HANDLING EXCEPTIONS
try :
    result = 10/0
except ZeroDivisionError:
    print("Can not divide by zero")    
#TRY-EXCEPT-ELSE-FINALLY
try :
    num = int(input("Please enter the value:\n"))
    result = 10/num
except ZeroDivisionError:
    print("Can not divide by zero")    
except ValueError :
    print("Invalid input! Please enter a valid number\n")
else :
    print(f"Result is {result}")
finally :
    print("Execution completed")

#RAISING EXCEPTION
def check_age(age):
    if age < 0:
        raise ValueError("The age can not negative")
    return "Valid age"


try :
    print(check_age(1))
except ValueError as e :
    print(f"error is {e}")



def find_valid_age(age):
    print(f"The age of the user is {age}")
    if age < 0:
        raise ValueError("The age not be negative")
    if type(age) != int:
        raise TypeError("Please enter a valid age")
    
    if age < 18:
        return f"The user has a valid age to vote -> {age}"
    else :
        return f"The user does not have a valid age -> {age}"
    
    

try :
    (find_valid_age("19"))
except ValueError as e :
    print(f"error : {e}")
except TypeError as ee :
    print(f"error : {ee}")


    
            
            