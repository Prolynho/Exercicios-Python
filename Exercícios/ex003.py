a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
sumOf = a + b
print('a soma entre {}{}{} e {}{}{} é igual a {}{}{}'
      .format('\033[1:35m', a, '\033[m', '\033[1:36m', b, '\033[m', '\033[1:33m', sumOf, '\033[m'))
