from math import hypot
legX = float(input('Opposite leg: '))
legY = float(input('Adjacent leg: '))
hypotenuse = hypot(legX, legY)
print('Hypotenuse: {:.2f}'.format(hypotenuse))
