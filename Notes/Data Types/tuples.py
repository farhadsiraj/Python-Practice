# ***** Tuples

# Tuples can hold various data types
my_tuple = (1, "two", 3.0)


letters = ("a", "a", "b")

# .count() returns the number of time an element exists in the tuple
print(letters.count("a"))

# .index() returns the index of the FIRST instance of an element
print(letters.index("a"))


# Tuples are similar to lists EXCCEPT they are immutable, once an element is assigned it cannot be changed
my_list = [1, 2, 3]
my_list[0] = "NEW"
print(my_list)

# my_tuple[0] = "NEW" *** This will cause an error
# print(my_tuple)
