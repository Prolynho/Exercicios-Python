'''
Crie um programa que leia o nome completo de uma pessoa
com todas as letras maiúsculas, minúsculas,
quantas letras ao todo (sem considerar espaço)
e quantas letras tem o primeiro nome:
'''
name = input('Insert your name: ')
print("""So, your name is {}.
Upper: {}
Lower: {}
Length: {}
Length (1st name): {}
""".format(name, name.upper(), name.lower(), len(name.replace(' ', '')), len(name.split()[0])))
