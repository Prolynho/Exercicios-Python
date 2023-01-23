carSpeed = float(input('Insert the speed of the car (Km/h): '))
if carSpeed >= 80:
    fine = float(carSpeed * 7)
    print('Sorry, you have been fined! You will have to pay R${:.2f}'.format(fine))
else:
    print('Very well, you are below the limit!')
