def pretty_sum(func):
    def wrapper(num1 , num2):
        print("Printing the sum")
        print(str(num1) + " + " + str(num2) + " = " , end= "")
        func(num1 , num2)
    return wrapper


@pretty_sum
def add(a , b ):
    sum = a+b
    print(sum)

add(10,20)