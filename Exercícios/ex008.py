meter = float(input('Insert value (M): '))
centimeter = meter * 100
millimeter = meter * 1000
colors = {'clear':  '\033[m',
          'red':    '\033[1:31m',
          'yellow': '\033[1:33m',
          'green':  '\033[1:32m'}
print('Meter = {}{:.2f}{}\nCentimeter = {}{:.2f}{}\nMillimeter = {}{:.2f}{}'
      .format(colors['red'], meter, colors['clear'],
              colors['yellow'], centimeter, colors['clear'],
              colors['green'], millimeter, colors['clear']))
