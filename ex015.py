days = int(input('How many days rented? '))
kilometer = float(input('How many KM traveled? '))
price = (days * 60) + (kilometer * 0.15)
print('The total price is R${:.2f}'.format(price))
