import random
import sys

win = 0
loss = 0
tie = 0
print()
print('x' * 198)
print()
print(' ' * 100, 'ROCK, PAPER, SCISSORS')
print()
print(f'{win} Wins, {loss} Losses, {tie} Ties')

while True:
    print()
    user_input = input('Enter your move: ROCK, PAPER, SCISSORS or QUIT : ')

    if user_input == 'ROCK':
        print()
        print('ROCK versus...')
        computer_move = random.randint(1, 3)
        if computer_move == 1:
            print('ROCK')
            tie += 1
        elif computer_move == 2:
            print('PAPER')
            loss += 1
        else:
            print('SCISSORS')
            win += 1
    elif user_input == 'PAPER':
        print()
        print('PAPER versus...')
        computer_move = random.randint(1, 3)
        if computer_move == 1:
            print('ROCK')
            win += 1
        elif computer_move == 2:
            print('PAPER')
            tie += 1
        else:
            print('SCISSORS')
            loss += 1
    elif user_input == 'SCISSORS':
        print()
        print('SCISSORS versus...')
        computer_move = random.randint(1, 3)
        if computer_move == 1:
            print('ROCK')
            loss += 1
        elif computer_move == 2:
            print('PAPER')
            win += 1
        else:
            print('SCISSORS')
            tie += 1

    elif user_input == 'QUIT':
        print()
        print('Thank You For Playing.')
        print(f'Your Score at the end is : {win} Wins, {loss} Losses, {tie} Ties.')
        print()
        print('x' * 198)
        sys.exit()
    else:
        print()
        print('Please Enter One of the Given Choices. (USE ONLY BLOCK LETTERS AS THE PROGRAMMER OF THIS PROGRAM IS '
              'VERY LAZY.)')
        continue

    print()
    print(f'{win} Wins, {loss} Losses, {tie} Ties')
