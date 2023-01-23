'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
number = randint(0, 5)
guess = int(input("Insert a number (0 to 5) and I'll try to guess: "))
if guess == number:
    print('Congratulations! You have won!')
else:
    print('GAME OVER! Better luck next time!')
