a = int(input('Insert 1st number: '))
b = int(input('Insert 2nd number: '))
c = int(input('Insert 3rd number: '))
if a > b > c:
    print("""Highest value: {} 
Lowest value: {}""".format(a, c))
elif a > c > b:
    print("""Highest value: {}
Lowest value: {}""".format(a, b))
elif b > a > c:
    print("""Highest value: {}
Lowest value: {}""".format(b, c))
elif b > c > a:
    print("""Highest value: {}
Lowest value: {}""".format(b, a))
elif c > b > a:
    print("""Highest value: {}
Lowest value: {}""".format(c, a))
elif c > a > b:
    print("""Highest value: {}
Lowest value: {}""".format(c, b))
