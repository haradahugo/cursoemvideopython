## Número real e porção inteira
from math import ceil, floor,trunc
num = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}.'.format(num, floor(num)))

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num,trunc(num)))