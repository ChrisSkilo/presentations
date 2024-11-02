# To write our decorator will need to write a function that:
#   1. Takes a function as an argument.
#   2.Has an inner function defined inside of it.
#   3.Returns the inner function.

def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

def get_called():
    print("I am the function and I am being called.")

# we have our decorator and our function to pass in 
# get_called = decorator(get_called)
# get_called()


#we can have the decorative step with the @ symbol
def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

# @decorator
# def get_called():
#     print("I am the function and I am being called.")

# #Calling the decorated function
# get_called()

# the two options for invoking operator are:
   # A function_call() or @pie-syntax


#The primary function of decorators is reducing the amount of code 
#that you need to write in your applications
def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)
# wash_dishes(1000)
chop_vegetables(1200)