'''
Conversor de temperaturas: escreva um programa 
que converta uma temperatura digitada em ºC para ºF
'''
celsius = float(input('Insert the value in °C: '))
fahrenheit = (celsius * 9/5) + celsius
print('converting the value to fahrenheit is equivalent to {:.2f}°F'.format(fahrenheit))
