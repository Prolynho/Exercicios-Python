# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
city = input('Insert your city: ').strip()
print("""So, your city is {}.
Have Santo: {}
""".format(city, city[:5].upper() == 'SANTO'))
