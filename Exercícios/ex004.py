'''Faça um programa que leia algo pelo teclado 
e mostre na tela o seu tipo primitivo 
e todas as informações possíveis sobre ele'''
inputOf = input('Digite algo: ')
colors = {'clear':  '\033[m',
          'yellow': '\033[33m',
          'green':  '\033[1;32m',
          'red':    '\033[1;31m',
          'redb':   '\033[1;30;41m'}
print('Tipo Primitivo: {}{}{}'.format(colors['yellow'], type(inputOf), colors['clear']))
print('É numérico: {}{}{}'.format(colors['green'], inputOf.isnumeric(), colors['clear']))
print('É alfabético: {}{}{}'.format(colors['red'], inputOf.isalpha(), colors['clear']))
print('É alfanumérico: {}{}{}'.format(colors['redb'], inputOf.isalnum(), colors['clear']))
print('É um espaço: {}{}{}'.format(colors['yellow'], inputOf.isspace(), colors['clear']))
print('Todas são maiúsculas: {}{}{}'.format(colors['yellow'], inputOf.isupper(), colors['clear']))
print('Todas são minúsculas: {}{}{}'.format(colors['yellow'], inputOf.islower(), colors['clear']))
print('Está capitalizada: {}{}{}'.format(colors['yellow'], inputOf.istitle(), colors['clear']))
