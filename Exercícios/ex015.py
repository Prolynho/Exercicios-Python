'''
Aluguel de carros: 
Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
'''
days = int(input('How many days rented? '))
kilometer = float(input('How many KM traveled? '))
price = (days * 60) + (kilometer * 0.15)
print('The total price is R${:.2f}'.format(price))
