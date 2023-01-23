'''
Faça um programa que leia um número inteiro 
qualquer e mostre na tela a sua tabuada
'''
value = int(input('Insert value: '))
colors = {'yellow':  '\033[1:33m',
          'magenta': '\033[1:35m',
          'cyan': '\033[1:36m'}
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 1, colors['magenta'], value*1))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 2, colors['magenta'], value*2))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 3, colors['magenta'], value*3))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 4, colors['magenta'], value*4))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 5, colors['magenta'], value*5))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 6, colors['magenta'], value*6))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 7, colors['magenta'], value*7))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 8, colors['magenta'], value*8))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 9, colors['magenta'], value*9))
print('{}{} x {}{} = {}{}'.format(colors['yellow'], value, colors['cyan'], 10, colors['magenta'], value*10))
