import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors\n"))
print(f"The user choice{game_choice[user_choice]}")
computer_choice = random.randint(0, 2)
print(f"computer choice {game_choice[computer_choice]}")
print(f"the computers choice is {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > 2 or user_choice < 0:
    print("you typed and invalid number")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice == computer_choice:
    print("It's a draw")


