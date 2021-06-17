## Catetos e hipotenusa
from math import sqrt, pow

cat1 = float(input('Digite o valor em cm do primeiro cateto: '))
cat2 = float(input('Digite o valor em cm do segundo cateto: '))
hip = sqrt(pow(cat1,2)+pow(cat2,2))
print('Os catetos {:.2f} e {:.2f} tem como hipotenusa {:.2f}'.format(cat1, cat2, hip))