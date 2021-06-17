## Soma ímpares múltiplos de três

s = 0

for imp in range(1,501):
    if imp % 3 == 0 and imp % 2 !=0:
        s += imp
print('A soma entre todos os números ímpares e múltiplos de 3 no intervalo de 1 a 500 é de {}.'.format(s))