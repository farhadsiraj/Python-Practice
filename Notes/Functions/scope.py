# ***** Scope


y = 25


def printer():
    y = 50
    return y


print(y)
print(printer())

"""
LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
"""

# GLOBAL
name = "THIS IS A GLOBAL STRING"


def greet():
    # ENCLOSING
    name = "Sammy"

    def hello():
        # LOCAL
        name = "Farhad"
        print("Hello " + name)

    hello()


greet()


x = 50


def func(x):
    print(f"x is {x}")
    x = 200
    print(f"I JUST LOCALLY CHANGED x to {x}")


func(x)
print(x)

# To change a global var using a function, instead of passing in the global variable, you can declare the global variable in the function scope.
# Any changes made to the global variable in the function scope will affect the variable globally.
# This is generally not recommended because you may accidently overwrite a global variable and it may not be obvious where the change occured.
def func2():
    global x
    print(f"x is {x}")
    x = 200
    print(f"I JUST LOCALLY CHANGED THE GLOBAL x to {x}")


func2()
print(x)
