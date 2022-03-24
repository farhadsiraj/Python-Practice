# ***** Functions

# Functions are created with the def keyword
def hello(name):
    """
    Triple quotes for
    multi-line comments
    """
    print(f"Hello, {name}!")


hello("Farhad")


def add(num1, num2):
    return num1 + num2


result = add(2, 5)
print(result)


def is_even(number):
    return number % 2 == 0


# print(is_even(22))
# print(is_even(15))


# Return true if ANY number is even inside a list


def check_even_list(list):
    for num in list:
        if num % 2 == 0:
            return True
        # else:
        #     pass
    return False


print(check_even_list([1, 3, 5]))

print(check_even_list([1, 3, 6]))

# Return all the even numbers in a list
def return_even_list(list):
    result = []
    for num in list:
        if num % 2 == 0:
            result.append(num)
        # else:
        #     pass
    return result


print(return_even_list([1, 2, 3, 4, 5]))


# Tuple unpacking
stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]

for ticker, price in stock_prices:
    print(ticker)

work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee

    return (employee_of_the_month, current_max)


# Tuple unpacking with a function call
name, hours = employee_check(work_hours)
print(name)
print(hours)
