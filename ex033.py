## Maior e Menor Valores

n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
n3 = int(input('Digite aqui o terceiro número: '))

maior = n1

if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3

print('O maior valor é o {}.'.format(maior))

menor = n1

if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3

print('O menor valor é o {}.'.format(menor))