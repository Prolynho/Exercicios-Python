from random import choice
names = [input('1st name: '), input('2nd name: '), input('3rd name: '), input('4th name: ')]
random = choice(names)
print('Selected name: {}'.format(random))
