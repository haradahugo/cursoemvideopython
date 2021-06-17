## Progressão Aritmética v2.0
a1 = int(input('Digite aqui o valor do primeiro termo: '))
r = int(input('Digite aqui a razão: '))
cont = 1
termo = a1
while cont <= 10:
    print('{} → '.format(termo), end = '')
    termo += r
    cont += 1
print('FIM')