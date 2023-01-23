'''
Faça um programa que leia uma frase qualquer e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
'''
phrase = input("Insert a phrase: ").upper().strip()
print("""Letter A Counter: {}
First Appearance: {}
Last Appearance: {}
""".format(phrase.count('A'), phrase.find('A')+1, phrase.rfind('A')+1))
