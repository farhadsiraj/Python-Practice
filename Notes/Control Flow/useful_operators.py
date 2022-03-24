# ***** Useful Operators

# range() generates numbers with the given start, stop, and step. DOES NOT create a list
for num in range(10):
    print(num)

for num in range(2, 10, 2):
    print(num)

# To create a list with range use list()
range_list = list(range(10))
print(range_list)

# enumerate() creates indexes for any iterable structure
word = "abcde"
for index, letter in enumerate(word):
    print(index, letter)

# zip() will combine multiple lists into a list of tuples. It will only combine up to the shortest list.
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ["a", "b", "c"]
mylist3 = ["red", "blue", "green"]

zip_list = list(zip(mylist1, mylist2, mylist3))
print(zip_list)

for item in zip_list:
    print(item)

# The 'in' operator will return a boolean when checking if an item is in an iterable structure
print("x" in [1, 2, 3])
print("a" in "Farhad")

d = {"mykey": 123}
print("mykey" in d)
print(123 in d.values())


# min() and max()
numbers = [6, 5, 7, 1, 3, 77, 34, 87, 3, 43]
print(min(numbers))
print(max(numbers))

# ***** Random library
from random import shuffle
from random import randint

# shuffle() will shuffle the elements in a list IN PLACE
shuffle(numbers)
print(numbers)

# randint(min, max) returns a random int in the given range
random_num = randint(0, 100)
print(random_num)

# input('string') will display the string to the user and ask for an input response. Always returns a STRING
# result = input("What's your name?\n")
# print(f"Hello, {result}")

# List Comprehensions
myString = "Hello"
listComp = [letter for letter in myString]
print(listComp)

listComp = [x for x in "word"]
print(listComp)

# Creating a list from 0-10 and squaring each element
numArr = [num**2 for num in range(0, 11)]
print(numArr)

# Creating a list from 0-10 with only even numbers
numArr = [num for num in range(0, 11) if num % 2 == 0]
print(numArr)

# Converting list of temperatures
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

# Writing if/else statements in list comprehension is NOT recommended because its a hard to read one liner and also differs from just if statements
results = [x if x % 2 == 0 else "ODD" for x in range(0, 11)]
print(results)

# Writing nested loops in list comprehension is ALSO NOT recommended because its a hard to read one liner
mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)
print(mylist)

mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)

# Ternary
# a if condition else b
"true" if True else "false"
"true" if False else "false"
