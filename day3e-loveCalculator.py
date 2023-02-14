# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name = name1 + name2

t = name.lower().count("t")
r = name.lower().count("r")
u = name.lower().count("u")
e = name.lower().count("e")

l = name.lower().count("l")
o = name.lower().count("o")
v = name.lower().count("v")
e = name.lower().count("e")

true = str(t + r + u + e)
love = str(l + o + v + e)

love_score = true + love
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
