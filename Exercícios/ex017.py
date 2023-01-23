'''
Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) 
e do cateto adjacente (ca) de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot
legX = float(input('Opposite leg: '))
legY = float(input('Adjacent leg: '))
hypotenuse = hypot(legX, legY)
print('Hypotenuse: {:.2f}'.format(hypotenuse))
