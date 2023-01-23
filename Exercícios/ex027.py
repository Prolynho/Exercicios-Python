'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente
'''
name = input('Insert your name: ')
print("""So, your name is {}
First Name: {}
Last Name: {}
""".format(name, name.split()[0], name.split()[-1]))
