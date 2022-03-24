# ***** String

"Hello"
print("Hello"[0])
print("Hello"[-1]) # print last letter of string with negative indexing
print("123" + "456")

# use len() to get the length of a string
len("Hello World!")


# string[start:stop:step]
# start is the numerical starting index 
# stop is the index you will go up to (but not include)
# step is the size of the "jump"

my_string = "abcdefghijk"
print(my_string[2:]) # print from "c" to the end
print(my_string[:3]) # print up to "c" (up to but not including index 3)
print(my_string[3:6]) # print "def"
print(my_string[::2]) # print every other letter starting with "a"
print(my_string[::-1]) # print in reverse (by taking backward steps)

name = "Sam"
print(name)
# Strings are immutable
# name[0] = "P" will not work because you can't change part of a string

# Concatination
last_letters = name[1:]
name = 'P' + last_letters 
print(name)

# Muliplication with letters
letters = 'z'
print(letters * 10)

# String Methods
x = "Hello, World. Today is a beautiful day. It's almost time for lunch!"
print(x.upper())
print(x.lower())
print(x.split())
print(x.split('.'))

# STRING.format()
print("This is a string {}".format('INSERTED'))
print('The {2} {1} {0}'.format('fox','brown','quick')) # can insert index in {} to use the word from the list at that index
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick')) 

# Float formatting => {value:width.precision f}
result = 100/777
print("The result was {r:1.3f}".format(r=result))

# f-String (string interpolation)
name = "Jose"
print(f"Hello, his name is {name}")

score = 100
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")