from random import randint
number = randint(0, 5)
guess = int(input("Insert a number (0 to 5) and I'll try to guess: "))
if guess == number:
    print('Congratulations! You have won!')
else:
    print('GAME OVER! Better luck next time!')
