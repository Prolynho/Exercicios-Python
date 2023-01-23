'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo
'''
a = int(input('Insert the first segment: '))
b = int(input('Insert the second segment: '))
c = int(input('Insert the third segment: '))
if a < b + c and b < a + c and c < a + b:
    print('You can make a triangle!')
else:
    print('You can not make a triangle!')
