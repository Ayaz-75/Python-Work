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

#Write your code below this line 👇
game_list = [rock, paper, scissors]
computer_choice = random.choice(game_list)
your_choice = game_list[(int(input("What do you choose ? type 0 for rock, 1 for paper and 2 for scissor\n")))]

if computer_choice == game_list[0] and your_choice == game_list[2]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You lose 😭")

elif computer_choice == game_list[2] and your_choice == game_list[0]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You win! 😍")

elif computer_choice == game_list[2] and your_choice == game_list[1]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You lose 😭")

elif computer_choice == game_list[1] and your_choice == game_list[2]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You win! 😍")

elif computer_choice == game_list[1] and your_choice == game_list[0]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You lose 😭")

elif computer_choice == game_list[0] and your_choice == game_list[1]:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\n You win! 😍")

else:
    print(f"computer choice:\n{computer_choice}, '\nyour choice: ' \n{your_choice}\nDraw🤣🤣🤣🤣🤣🤣🤣")

