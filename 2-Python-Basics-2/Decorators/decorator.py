def hello(func):
    
    def inner():
        print("Start")
        func()
        print("End")
    return inner

def name():
    print("Rahul Mishra")


obj = hello(name)
obj()


def who():
    print("Rahul Mishra")

def display(func):
    def inner_function():
        print("Start")
        print("The current user is : " , end= '')
        func()
        print("End")
    return inner_function

if __name__ == "__main__" :
    myobj = display(who)
    myobj()
    
    

def greeting():
    print("Hi , How are you !!")

def decorator_function(func1):
    def wrapper_function():
        print("Process start")
        func1()
        print("Process End")
    return wrapper_function


new_obj = decorator_function(greeting)
new_obj()
        
        
@decorator_function
def user():
    print("Rahul Mishra")

user()



