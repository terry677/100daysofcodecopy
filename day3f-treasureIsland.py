print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the missing treasure.")
choice1 = input("You are at a cross road, which way do you want to go? Left or Right? \n").lower()
score = 0
if choice1 == 'left':
    print("You fell into a hole and was pierced by thorns")
    print("Game over!!")
    print(f"your score is {score}")
else:
    print("You arrived at a river bank.")
    choice2 = input("Do you want to swim or wait for a boat?\n").lower()
    if choice2 == 'wait':
        print("A boat arrived and took you across in safety")
        choice3 = input("You arrived at three doors, do you want to open or wait? \n").lower()
        if choice3 == 'open':
            choice4 = input("Which door do you want to open? Red, Blue, Green \n").lower()
            if choice4 == 'red':
                print("The room was filled with fire and you got burnt")
                print("Game Over")
                score += 30
                print(f"your score is {score}")
            elif choice4 == 'blue':
                print("You were eaten by beast")
                print("Game Over")
                score += 30
                print(f"your score is {score}")
            elif choice4 == 'green':
                print("Congratulations!! you found the treasure")
                print("You Win.")
                score += 40
                print(f"your score is {score}")
        else:
            print("You were attacked by aliens")
            print("Game Over!!")
            score += 20
            print(f"your score is {score}")

    else:
        print("You were attacked by a trout and died.")
        print("Game Over")
        score += 10
        print(f"your score is {score}")


