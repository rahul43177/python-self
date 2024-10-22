import time as T
import math 
def time_calculator(func):
    def wrapper(*arg):
        start_time = T.time()
        print(f"Start time -> {start_time}")
        func(*arg)
        end_time = T.time()
        print(f"End time -> {end_time}")
        time_to_execute = math.floor(end_time - start_time)
        print("The function took " + str(time_to_execute) + " seconds to execute")
    return wrapper

@time_calculator
def add_two_number(a , b , seconds):
    T.sleep(seconds)
    sum = a+b
    print("The sum of two numbers are " + str(sum))

add_two_number(10 , 20 , 2)
