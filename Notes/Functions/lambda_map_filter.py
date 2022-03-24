# ***** Map


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

# map will apply the function to every item in an iterable structure (list, tuple, etc).
for item in map(square, my_nums):
    print(item)

# map function returns a map object, to iterate through the result, use a list
result = list(map(square, my_nums))

print(result)


def splicer(string):
    if len(string) % 2 == 0:
        return "EVEN"
    else:
        return string[0]


names = ["Andy", "Eve", "Sally"]

print(list(map(splicer, names)))

# ***** Filter


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(check_even, my_nums))

print(evens)

# ***** lambda expressions (anonymous functions)


def squared(num):
    result = num**2
    return result


lambda_squared = lambda num: num**2
print(lambda_squared(3))

print(list(map(lambda num: num**2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))
