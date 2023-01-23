# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
value = int(input('Insert value: '))
double = value * 2
triple = value * 3
squareRoot = value ** (1/2)
colors = {'red':    '\033[1:31m',
          'yellow': '\033[1:33m',
          'green':  '\033[1:32m',
          'clear':  '\033[m'}
print('Double = {}{}{}\nTriple = {}{}{}\nSquare Root = {}{}{}'
      .format(colors['red'], double, colors['clear'],
              colors['yellow'], triple, colors['clear'],
              colors['green'], squareRoot, colors['clear']))
