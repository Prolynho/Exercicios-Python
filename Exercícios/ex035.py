a = int(input('Insert the first segment: '))
b = int(input('Insert the second segment: '))
c = int(input('Insert the third segment: '))
if a < b + c and b < a + c and c < a + b:
    print('You can make a triangle!')
else:
    print('You can not make a triangle!')
