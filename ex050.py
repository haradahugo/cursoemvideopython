## Soma dos pares

n1 = int(input('Digite aqui o primeiro número: '))
n2 = int(input('Digite aqui o segundo número: '))
n3 = int(input('Digite aqui o terceiro número: '))
n4 = int(input('Digite aqui o quarto número: '))
n5 = int(input('Digite aqui o quinto número: '))
n6 = int(input('Digite aqui o sexto número: '))

s=0

for pares in n1,n2,n3,n4,n5,n6:
    if pares % 2 == 0:
        s += pares
print('A soma dos números pares resultou em {}.'.format(s))