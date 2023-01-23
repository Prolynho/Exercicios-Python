'''
Desafio 16: Crie um programa que leia um número real 
qualquer pelo teclado e mostre na tela a sua porção inteira.
'''
from math import trunc
num = float(input('Insert value: '))
truncate = trunc(num)
print('Truncated value: {}'.format(truncate))
