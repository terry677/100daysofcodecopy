print("Welcome to the roller-coaster!")
height = int(input("Enter your height in cm: \n"))
bill = 0
if height <= 120:
    print("Can't ride on the roller-coaster!, sorry you have to grow taller.")
else:
    print("Can ride on the roller-coaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age <= 18:
        print("Please pay $7")
        bill = 7
    elif (age >= 45) and (age <= 55):
        bill = 0
    else:
        print("Please pay $12")
        bill = 12
    photo = input("Do you want to take a photo? ('Y' or 'N')\n")
    if photo == 'Y':
        bill += 3
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")

