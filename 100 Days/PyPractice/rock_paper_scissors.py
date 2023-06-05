import random

print("welcome to rock paper and scissor project")
print()
# Rock Paper Scissors ASCII Art
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


user_choice = int(input("Enter your choice '0' for rock '1' for paper and '2' for scissor: "))
computer_chosen = random.randint(0, 2)

if user_choice == 0 and computer_chosen == 2:
    print("you chose: ", rock, "\nComputer chose: \n", scissor, " You win")
elif computer_chosen == 0 and user_choice == 2:
    print("you chose: ", scissor, "\nComputer chose: \n", rock, " You loose")
elif user_choice == 0 and computer_chosen == 0:
    print("you chose: ", rock, "\n computer chose: \n", rock, " Tie")


elif user_choice == 2 and computer_chosen == 1:
    print("you chose: ", scissor, "\nComputer chose: \n", paper, " You win")
elif computer_chosen == 2 and user_choice == 1:
    print("you chose: ", scissor, "\nComputer chose: \n", paper, " You loose")
elif user_choice == 1 and computer_chosen == 1:
    print("you chose: ", paper, "\n computer chose: \n", paper, " Tie")


elif user_choice == 1 and computer_chosen == 0:
    print("you chose :", paper, "\ncomputer chose: \n", rock, " you win")
elif computer_chosen == 1 and user_choice == 0:
    print("you chose: ", rock, "\nComputer chose: \n", paper, " you loose")
elif user_choice == 2 and computer_chosen == 0:
    print("you chose: ", scissor, "\n computer chose: \n", scissor, " Tie")
