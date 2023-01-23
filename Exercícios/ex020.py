'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle
names = [input('1st name: '), input('2nd name: '), input('3rd name: '), input('4th name: ')]
shuffle(names)
print('Shuffled names: {}'.format(names))
