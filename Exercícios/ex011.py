'''
Faça um programa que leia a largura e a algura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2m²
'''
width = float(input('Insert the width: '))
height = float(input('Insert the height: '))
area = (width * height)
paint = area / 2
print('You need {:.2f} liters to paint {:.2f}m²'.format(paint, area))
