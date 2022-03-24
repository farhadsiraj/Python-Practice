# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = "Print only the words that start with s in this sentence"

st = st.split()
print(st)
for word in st:
    if word[0].lower() == "s":
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11):
    if num % 2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
div3 = [num for num in range(1, 51) if num % 3 == 0]
print(div3)

# Go through the string below and if the length of a word is even print "even!"

st = "Print every word in this sentence that has an even number of letters"
st = st.split()
for word in st:
    if len(word) % 2 == 0:
        print(word + " EVEN")


# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = "Create a list of the first letters of every word in this string"
first_letters = [word[0] for word in st.split()]
print(first_letters)
