'''
Desenvolva um programa que leia as duas notas 
de um aluno, calcule e mostre a sua média
'''
noteX = float(input('Insert the first note: '))
noteY = float(input('Insert the second note: '))
average = ((noteX + noteY) / 2)
print('Average Note: {}{:.1f}{}'.format('\033[1:32m', average, '\033[m'))
