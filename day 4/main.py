
import random

print('''


                welcome to the rockpaper sciecors game!
      ''')



user = input('Select 1 or paper 2 for scissors and 3 for rock: ')
computer = random.randint(0,3)

paper = 1
rock = 3
sc = 2

if not user.isdigit():
    print('Please enter a number not a letter or character')
else:
    user = int(user)
    if user > 3:
        print('Pleae enter a number in the specified range and try again.')

    else:
        if user ==1 or user ==2 or user ==3:
            if user ==1:
                print(f'Yout choose paper')
            elif user ==2:
                print(f'You choose scissor')
            else:
                print('You choose Rock')

            if user ==0 and computer ==0:
                print('DRAW')
            elif user == computer:
                print(f'The computer also selects {user}')
                print(f'You win')
            else:
                print(f'You choose {user} and the computer chooses {computer}')
                print('You loose')

