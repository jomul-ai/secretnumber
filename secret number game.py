import random
num = random.randint(1,101)
print(num)

print('\nWELCOME TO THE GUESSING NUMBER GAME:',end='')
print('''
      1. Guess a number from 1-100
      2. You will have 3 attempts
      3. Good luck!''')

guess = int(input('\nGuess a number from 1-100: '))

while True:
    if guess < num:
        print('The number is too small!')
        guess = int(input('\nGuess again: '))
    elif guess > num:
        print('The number is too big!')
        guess = int(input('\nGuess again: '))
    elif guess == num:
        print('\nYou are correct!')
        break