# ***** Lists

list1 = [1,2,3]
list2 = ["STRING", 100, 23.2]
list3 = ['one','two','three']

# Lists also use indexing and slicing
print(list2[0])
print(list3[:2])
print(list3[1:])

# Lists can be concatinated
new_list = list1 + list3
print(new_list)

# Lists are mutable
new_list[3] = 'ONE'
print(new_list)

# Add to a list with append()
new_list.append('A')
print(new_list)

# Remove an item from the end of the list with .pop()
end = new_list.pop()
print(new_list)
print(end)

# pop() can remove the given index position
start = new_list.pop(0)
print(new_list)
print(start)

# Lists can be sorted in place with sort() 
letters = ['q','w','e','r','t','y','a','s','d','f']
numbers = [9,1,8,3,7,2,6,5,4]
print(letters, numbers)

letters.sort()
numbers.sort()
print(letters, numbers)

# The sort method does NOT return anything so if you try to assign to a var the result will be NONE
sorted_letters = letters.sort()
print('WRONG',sorted_letters)

# To create a new variable with the sorted list you need to sort first then assign the new var the sorted list
letters.sort()
sorted_letters = letters
print('RIGHT',sorted_letters)

# Lists can be reversed in place with reverse()
numbers.sort()
numbers.reverse()
print(numbers)