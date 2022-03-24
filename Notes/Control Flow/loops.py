# ***** Loops *****

# ***** For Loops
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list:
    print(number)

# Conditional statements in for loop
for num in my_list:
    if num % 2 == 0:
        print(f"Even number: {num}")
    else:
        print(f"Odd number: {num}")

# Summing the elements in a list
list_sum = 0
for num in my_list:
    list_sum = list_sum + num

print(list_sum)

# If you don't need to use the variable you can use _
for _ in my_list:
    print("Cool!")

# Iterating through a string
my_string = "Hello World"
for letter in my_string:
    print(letter)

# Iterating through a list of tuples
my_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in my_tuples:
    print(item)

# Tuple unpacking
for a, b in my_tuples:
    print(a)
    print(b)

# Iterating through Dictionaries
# Since dictionaries are unordered there is no guarantee that when iterating through a dictionary the elements will be in the same order as they were created in
d = {
    "k1": 1,
    "k2": 2,
    "k3": 3,
}
# Iterating normally will only show the keys
for item in d:
    print(item)

# use .items() to show both keys and items
for item in d.items():
    print(item)

# Can use unpacking to split the key and value
for key, value in d.items():
    print(key)
    print(value)

# ***** While Loops
x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("X is not less than 5")

# break: Breaks out of the current closest enclosing loop.
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# continue: Goes to the top of the closest enclosing loop.
name = "Farhad"
for letter in name:
    if letter == "a":
        continue
    print(letter)

# pass: Does nothing at all. Used as filler or placeholder in loops when they are a work in progress
x = [1, 2, 3]
for item in x:
    pass
