travel = float(input('How far do you want to travel (KM)? '))
if travel <= 200:
    print('You will have to pay R${:.2f}'.format(travel * 0.50))
else:
    print('You will have to pay {:.2f}'.format(travel * 0.45))
