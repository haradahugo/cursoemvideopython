## Seno, cosseno e tangente
from math import radians,sin,cos,tan

ang = float(input('Digite um ângulo e obtenha seu seno, cosseno e tangente: '))
rad = radians(ang)

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('Para o ângulo de {:.1f}, os respectivos valores de seno, cosseno e tangente são: {:.3f}, {:.3f} e {:.3f}'.format(ang,sen,cos,tan))