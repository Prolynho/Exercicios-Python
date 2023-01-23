'''
Crie um programa que leia quanto dinheiro uma pessoa tem 
na carteira e mostre quantos dólares ela pode comprar
'''
real = float(input('How many money? R$'))
dollar = float(real / 5.45)
print('You have US${}{:.2f}{}'.format('\033[1:32m', dollar, '\033[m'))
