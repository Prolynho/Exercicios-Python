# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
number = input('Insert a number (0 to 9999): ')
print("""So, your number is {}.
Unit: {}
Dozen: {}
Hundred: {}
Thousand: {}
""".format(number, number[3], number[2], number[1], number[0]))
