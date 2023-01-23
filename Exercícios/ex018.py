from math import sin
from math import cos
from math import tan
from math import radians
angle = float(input('Insert radian: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('Sine: {:.2f}\nCosine: {:.2f}\nTangent: {:.2f}'.format(sine, cosine, tangent))
