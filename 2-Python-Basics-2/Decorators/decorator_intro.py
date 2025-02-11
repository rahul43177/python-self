# there are two decorators -> function decorators and class decorators 

def start_end_decorator(func):
    
    def wrapper(*args , ):
        print("Start")
        func()
        print("End")
    return wrapper
@start_end_decorator
def print_name():
    print("Rahul")


# print_name = start_end_decorator(print_name)
print_name()

@start_end_decorator
def add(x ,y):
    return x+y

print(add(10,20))



