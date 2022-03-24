# ***** Errors


def add(n1, n2):
    print(n1 + n2)


add(10, 20)


# This will cause an TypeError because input returns a string.  Without the try/catch the rest of the script would be interupted
try:
    add(10, "20")
except:
    print("This errors because you can't add a number and string")
else:
    print("hello")


try:
    result = 10 + 10
except:
    print("Error")
else:
    print(f"The result is {result}")


# You can create excepts for specific errors. Putting a general except at the end will catch all other errors. The following will induce an OS Error
try:
    f = open("testfile", "r")
    f.write("Write a test line")
except TypeError:
    print("There was a TypeError")
except OSError:
    print("There was an OS Error")
except:
    print("All other errors")
finally:
    print("This always execute")


def ask_for_int():
    while True:
        try:
            result = int(input("Number?"))
        except:
            print("Not a number")
            continue
        else:
            print(f"Your input is {result}")
            break
        finally:
            print("End of try/except/finally")


ask_for_int()
