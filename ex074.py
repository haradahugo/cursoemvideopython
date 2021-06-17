## Maior e menor valores em tupla
from random import randint
n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)
tupla = (n1,n2,n3,n4,n5)
maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5
    
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5
print(f'A tupla é a seguinte {tupla}\nO maior valor é {maior}\nO menor valor é {menor}')