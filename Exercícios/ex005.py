'''
Faça um programa que leia um número inteiro
e mostre na tela seu sucessor e antecessor
'''
value = int(input('Insert value: '))
colors = {'clear': '\033[m',
          'red':   '\033[1:31m',
          'green': '\033[1:32m'}
successor = value + 1
predecessor = value - 1
print('Successor = {}{}{}\nPredecessor = {}{}{}'
      .format(colors['green'], successor, colors['clear'], colors['red'], predecessor, colors['clear']))
