# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_persons = random.randint(0, (len(names) - 1))
print(f"{names[number_of_persons]} is going to buy the meal today!")

