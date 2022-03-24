# ***** *args amd **kwargs(key word arguments)


def myfunc(a, b):
    # returns 5% of the sum of a and b
    # sum() function takes in a tuple
    return sum((a, b)) * 0.05


print(myfunc(40, 60))

# '*' allows for any number of arguments. Arguments are stored as a tuple
def myfunc2(*args):
    return sum(args) * 0.05


print(myfunc2(40, 60, 1, 6, 11))

# '**' allows for key word arguments, stored as a dictionary
def myfunc3(**kwargs):
    if "fruit" in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not find any fruit here")


myfunc3(fruit="apple", veggie="lettuce")
myfunc3(veggie="lettuce")


def myfunc4(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")


myfunc4(10, 20, 30, fruits="orange", food="eggs", animal="dog")
