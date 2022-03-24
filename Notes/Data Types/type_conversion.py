# ***** Typechecking and Conversion

# To check datatype use type()
print(type("Hello"))

length = len(input("What is your name?"))

# use str() to convert to a string
length_str = str(length)

print("Your name has " + length_str + " characters.")


two_digit_number = input("Type a two digit number: ")

# use int() to convert to an integer
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
print(num1 + num2)

# use float to convert to a float
print(float(num1 + num2))
