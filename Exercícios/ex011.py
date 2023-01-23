width = float(input('Insert the width: '))
height = float(input('Insert the height: '))
area = (width * height)
paint = area / 2
print('You need {:.2f} liters to paint {:.2f}m²'.format(paint, area))
