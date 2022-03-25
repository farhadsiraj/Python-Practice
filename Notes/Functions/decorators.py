# ***** Decorators

# Functions can be defined within a function and can be returned from that function
# Decorators are used in web frameworks like Django or Flask


def hello(name="Jose"):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() function inside hello()"

    def welcome():
        return "\t This is the welcome() function inside hello()"

    print("I am going to return a function")

    if name == "Jose":
        return greet
    else:
        return welcome


hello()

my_new_func = hello()

print(my_new_func())

# Functions can be passed as arguments to another function
def hello():
    return "Hi Jose!"


def other(func):
    print("Other code runs here!")
    print(func())


other(hello)


# Decorators allow you to add new functionality to an existing function and switch it on/off


def new_decorator(original_func):
    def wrap_func():

        print("Some extra code, before original function")

        original_func()

        print("Some extra code, after original function")

    return wrap_func


# def func_needs_decorator():
#     print("I want to be decorated!!")


# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

# Using the decorator is the same as passing the function into another function, adding it to a variable and calling that variable (commented code above)
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()
