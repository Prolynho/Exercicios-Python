# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date
leapYear = int(input('Insert a year (insert 0 to analyze the actual date: '))
if leapYear == 0:
    leapYear = date.today().year
if leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0:
    print('The year {} is a leap year!'.format(leapYear))
else:
    print('The year {} is not a leap year!'.format(leapYear))
