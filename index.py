import random
number = random.randint(1,9)
print('Number Guessing game')
print('Guess a number (between 1 and 9)')
chances = 0
while chances < 5:
    guess = int(input('enter your guess'))
    if number == guess:
        print("congratulations")
        break 
    if guess<number:
        print('please enter a greater number')
    if guess>number:
        print('please enter a lower number')

    chances +=1

if not chances<5:
    print('you lost the game the correct answer is ',number)