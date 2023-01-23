'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
'''
from random import choice
names = [input('1st name: '), input('2nd name: '), input('3rd name: '), input('4th name: ')]
random = choice(names)
print('Selected name: {}'.format(random))
