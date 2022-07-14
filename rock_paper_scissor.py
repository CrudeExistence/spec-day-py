import random

computer_choice = random.choice(['scisosrs','rock','paper'])
user_choice = input('Do you want - rock, paper or scissors?\n')

if computer_choice == user_choice:
    print('TIE')
elif computer_choice == 'scissors' and user_choice == 'rock':
    print('WIN')
elif computer_choice == 'paper' and user_choice == 'scissors':
    print('WIN')
elif computer_choice == 'rock' and user_choice == 'paper':
    print("WIN")
else:
    print('You lose and the computer wins')


