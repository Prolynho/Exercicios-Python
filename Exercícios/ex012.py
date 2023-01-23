'''
Faça um algoritmo que leia o preço de um produto 
e mostre seu novo preço, com 5% de desconto
'''
price = float(input('Product price: '))
discountPrice = price - (price * 5/100)
print('New price: {:.2f}'.format(discountPrice))
