from random import shuffle
names = [input('1st name: '), input('2nd name: '), input('3rd name: '), input('4th name: ')]
shuffle(names)
print('Shuffled names: {}'.format(names))
