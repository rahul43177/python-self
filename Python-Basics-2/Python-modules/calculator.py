import addition #we have imported addition here and used it here
import substraction #we have imported substraction here and used it here

number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2 : "))
add = addition.add(number1 , number2)
print(f"The addition of {number1} and {number2} is {add}")
sub = substraction.sub(number1 , number2)
print(f"The substraction of {number1} and {number2} is {sub}")



