'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''
travel = float(input('How far do you want to travel (KM)? '))
if travel <= 200:
    print('You will have to pay R${:.2f}'.format(travel * 0.50))
else:
    print('You will have to pay {:.2f}'.format(travel * 0.45))
