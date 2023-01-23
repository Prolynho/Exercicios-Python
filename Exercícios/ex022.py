# Crie um programa que leia o nome completo de uma pessoa:
name = input('Insert your name: ')
print("""So, your name is {}.
Upper: {}
Lower: {}
Length: {}
Length (1st name): {}
""".format(name, name.upper(), name.lower(), len(name.replace(' ', '')), len(name.split()[0])))
