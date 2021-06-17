## Cálculo do Fatorial
num = int(input('Digite aqui um número para saber o seu fatorial: '))
fatorial = 1
i = 2
while i <= num:
    fatorial = fatorial * i
    i = i + 1
print('Resultado de {}! é {}.'.format(num, fatorial))