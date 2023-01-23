salary = float(input('How many is your salary? '))
if salary >= 1250:
    newSalary = salary + (salary * 10/100)
    print('your new salary is {:.2f}'.format(newSalary))
else:
    newSalary = salary + (salary * 15/100)
    print('your new salary is {:.2f}'.format(newSalary))
