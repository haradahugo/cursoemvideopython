## Maior e Menor Valores

i = int(input('Digite aqui um número inteiro: '))
continua = str(input('Deseja continuar [S/N]? ')).upper()
cont = 1
soma = 0
maior = i
menor = i
inicio = i

while continua == 'S':
    i = int(input('Digite aqui um número inteiro: '))
    if maior < i:
        maior = i
    else:
        maior = maior
    if menor > i:
        menor = i
    else: menor = menor
    cont += 1
    soma += i
    continua = str(input('Deseja continuar [S/N]? ')).upper()

print('\nA média dos valores digitados é de {}.\nO maior número digitado é o {}.\nO menor número digitado é o {}.'.format((soma + inicio)/cont, maior, menor))