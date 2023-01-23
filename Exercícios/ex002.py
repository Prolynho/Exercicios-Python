# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}{}{}!'.format('\033[1:34m', nome, '\033[m'))
