# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
name = input('Insert your name: ')
print("""So, your name is {}.
Have Silva: {}
""".format(name, 'silva' in name.lower()))
