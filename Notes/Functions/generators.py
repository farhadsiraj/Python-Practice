# ***** Generators

# This function creates a list of cubes in memory and returns the list
from re import A


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


print(create_cubes(10))

for x in create_cubes(10):
    print(x)

# This function generates the cubes one at a time, using the previous result to determine the next result. This way an entire list does not need to be put in memory


def create_cubes_generator(n):
    for x in range(n):
        yield x**3


# Yield does not return so if you do need a list you need to cast using list()
list(create_cubes_generator(10))

for x in create_cubes_generator(10):
    print(x)


def gen_fibonacci(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibonacci(10):
    print(number)


# Using next()


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

# Note the function is being called
g = simple_gen()

print(g)
print(next(g))
print(next(g))
print(next(g))
# The 4th call results in a Stop Iteration error because the function only goes up to 3
# print(next(g))

# iter()

s = "hello"

for letter in s:
    print(letter)

# This will cause a TypeError because it's not directly iterable
# next(s)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
