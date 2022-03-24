# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        min(num1, num2)
    else:
        max(num1, num2)


print(lesser_of_two_evens(2, 4))  # 2
print(lesser_of_two_evens(2, 5))  # 5


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crackers(string):
    words = string.split()
    return words[0][0] == words[1][0]


print(animal_crackers("Levelheaded Llama"))  # True
print(animal_crackers("Crazy Kangaroo"))  # False


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False\


def makes_twenty(num1, num2):
    if 20 in [num1, num2]:
        return True
    else:
        return num1 + num2 == 20


print(makes_twenty(20, 10))  # True
print(makes_twenty(12, 8))  # True
print(makes_twenty(2, 3))  # False

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(string):
    # return string[0].upper() + string[1:3] + string[3].upper() + string[4:]
    return string[:3].capitalize() + string[3:].capitalize()


print(old_macdonald("macdonald"))  # MacDonald


# MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(string):
    # words = string.split(" ")
    # words.reverse()
    # words = " ".join(words)
    # return words
    return " ".join(string.split()[::-1])


print(master_yoda("I am home"))  # 'home am I'
print(master_yoda("We are ready"))  # 'ready are We'


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(num):
    if abs(num - 100) <= 10 or abs(num - 200) <= 10:
        return True
    else:
        return False


print(almost_there(90))  # True
print(almost_there(104))  # True
print(almost_there(150))  # False
print(almost_there(209))  # True

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(numlist):
    for i in range(0, len(numlist) - 1):
        if numlist[i] == 3 and numlist[i + 1] == 3:
            return True
    return False


print("Find 33")
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(string):
    result = ""
    for i in range(0, len(string)):
        result += string[i] * 3
    return result


print(paper_doll("Hello"))  # 'HHHeeellllllooo'
print(paper_doll("Mississippi"))  # 'MMMiiissssssiiippppppiii'


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif 11 in (a, b, c) and sum - 10 <= 21:
        return sum - 10
    else:
        return "BUST"


print(blackjack(5, 6, 7))  # 18
print(blackjack(9, 9, 9))  # 'BUST'
print(blackjack(9, 9, 11))  # 19


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(nums):
    sum = 0
    add = True
    for i in range(0, len(nums)):
        while add:
            if nums[i] != 6:
                sum += nums[i]
                break
            else:
                add = False
        while not add:
            if nums[i] != 9:
                break
            else:
                add = True
                break
    return sum


print(summer_69([1, 3, 5]))  # 9
print(summer_69([4, 5, 6, 7, 8, 9]))  # 9
print(summer_69([2, 1, 6, 9, 11]))  # 14


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(nums):

    code = [0, 0, 7, "x"]

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# By convention, 0 and 1 are not prime.


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(100))  # 25
