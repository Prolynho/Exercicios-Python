'''Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento
''
wage = float(input('Wage: '))
newWage = wage + (wage * 15/100)
print('New wage: {:.2f}'.format(newWage))
