name = input('Enter your name: ').title()
age = eval(input('Enter age: '))
print(f'Welcome Mr/Mrs {name}')
print()
print('------ Rock, Paper, Scissors Game! ------')

import random
myList = ['rock', 'paper', 'scissors']

while True:
    count = 0
    rounds = eval(input('How many times do you want to play? '))
    for i in range(rounds):
        user_choice = input('Enter your choice: ').lower()
        computer_choice = random.choice(myList)

        while user_choice not in myList:
            print('Please input choice from the list above!')
            user_choice = input('Enter your choice(Rock, Paper or Scissors): ').lower()
            count += 0
           
        while user_choice == computer_choice:
            print("It's a tie!")
            print(f'You choose {user_choice}')
            print(f'Computer choose {computer_choice}')
            user_choice = input('Enter your choice(Rock, Paper or Scissors): ').lower()
            computer_choice = random.choice(myList).lower()
        
        if ((user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
            print(f'You choose {user_choice}')
            print(f'Computer choose {computer_choice}')
            print('You won!')
            count += 1

        else:
            print(f'You choose {user_choice}')
            print(f'Computer choose {computer_choice}')
            print('You lose! Computer wins!')


    if count == rounds:
        print('Game over')
        
    print(f'You won {count} time(s) out of {rounds} rounds!')
    
    play_again = input('Do you wish to play again? (Yes or No): ').lower()
    if play_again == 'no':
        print('Thanks for playing')
        break
    while play_again != 'yes' and 'no':
        play_again = input('Do you wish to play again? (Yes or No): ').lower()

    if name == 'stop' or age == 'stop':
        break



