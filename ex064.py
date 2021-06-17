## Tratando vários valores v1.0
i = int(input('Digite aqui qualquer número inteiro, e digite 999 quando desejar parar de inputar dados: '))
cont = 0
soma = 0
inicio = i
while i != 999:
    i = int(input('Digite aqui qualquer número inteiro, e digite 999 quando desejar parar de inputar dados: '))
    cont += 1
    soma += i
print('\nVocê inputou {} dados, e a soma entre eles é de {}.'.format(cont, soma + inicio - 999))