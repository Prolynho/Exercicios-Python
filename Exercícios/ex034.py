'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
'''
salary = float(input('How many is your salary? '))
if salary >= 1250:
    newSalary = salary + (salary * 10/100)
    print('your new salary is {:.2f}'.format(newSalary))
else:
    newSalary = salary + (salary * 15/100)
    print('your new salary is {:.2f}'.format(newSalary))
