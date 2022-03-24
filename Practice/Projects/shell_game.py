# ***** Interactions between multiple Functions

# Import shuffle function from random
from random import shuffle

# example = [1, 2, 3, 4, 5, 6, 7]

# Shuffle mutates the list in-place
# shuffle(example)
# print(example)

# Create a function that returns the shuffled list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# Create a function that takes in a user input of 0-2 and returns the input
def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0,1, or 2\n")

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# Initial List
mylist = [" ", "O", " "]

# Shuffle List
mixed_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
check_guess(mixed_list, guess)
