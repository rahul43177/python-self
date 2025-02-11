def who():
    print("Rahul")


def display_user(func):
    def inner():
        print("Start")
        print("The last user who logged in was : " , end= "")
        func()
        print("End")
    return inner


obj = display_user(who)
obj()

# Self invoking decorator 
#This is Syntactic sugar  -> a nice way to write decorator
@display_user
def show_name():
    print("New user")

show_name()