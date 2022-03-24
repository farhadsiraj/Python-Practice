# ***** Sets

# Unordered collection of UNIQUE elements

# sets are created using set()
my_set = set()
print(my_set)

# .add() adds elements to the set
my_set.add(1)
my_set.add(2)
print(my_set)

# dupes are not added to sets
my_set.add(2)
print(my_set)

# use sets to find the unique values in a list
my_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
new_set = set(my_list)
print(new_set)
