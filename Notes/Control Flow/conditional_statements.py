# ****** Conditional Statements

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height < 120:
    print("Can't ride")
else:
    print("Can ride")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
