import random

print('Welcome to the number guessing game world!')

user_input = int(input('Guess any number between 1 and 10: '))

answer = random.randint(1,10)

if user_input == answer:
    print('You made it to the next leavel !! kudos!!!')

    print('Lets play another game (head or tail): ')
    user_input2 = input('Head or tail: ').lower()
    answer2 = random.choice(['head','tail'])

    if user_input2 == answer2:
        print('Well done you are a guessing master!!')
    else:
        print('Thank you men!!')
else:
    print('You lose!!')