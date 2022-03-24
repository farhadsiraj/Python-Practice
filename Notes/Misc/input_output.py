# ***** Input/Output

# Use open('filename') to open a file in the current directory. Filename needs to be in string. Errno 2 means the filename is wrong OR the directory is wrong
myfile = open("myfile.txt")

# .read() will display the text in the file
print(myfile.read())

# Running .read() in a row will return ' ' because the cursor was left at the end of the text from the previous run
print(myfile.read())

# To reset the cursor use .seek(0)
myfile.seek(0)
# print(myfile.read())

contents = myfile.read()
print(contents)

# .readlines() creates a list with each line as an element
myfile.seek(0)
lines = myfile.readlines()
print(lines)

# If you open a file with open() you need to close it to avoid errors
myfile.close()

# To avoid needing to close files, you can use "with open('filepath') as varName:".
# Any code within the indentation after the colon will run and the file will close by itself at the end
# Use a filepath to open a file from any directory
with open(
    "/Users/farhadsiraj/Documents/Python/Notes/myfile.txt",
) as new_file:
    contents = new_file.read()


# The open function has a mode paramater that controls permissions
# mode = 'r' is read only
# mode = 'w' is write only (will overwrite files or create new ones)
# mode = 'a' is append only (will add to files)
# mide = 'r+' is reading and writing
# mode = 'w+' is writing and reading (overwrites existing files or creates new files)

with open("newfile.txt", mode="r") as f:
    print(f.read())

with open("newfile.txt", mode="a") as f:
    f.write("\nFOUR ON FOURTH")

with open("newfile.txt", mode="r") as f:
    print(f.read())

with open("test.txt", mode="w") as f:
    f.write("I CREATED THIS FILE")
