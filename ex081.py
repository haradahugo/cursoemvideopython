## Extraindo dados de uma lista
lista = []
cont = 0
while True:
    lista.append(int(input('Digite aqui um número inteiro: ')))
    cont += 1
    pros = str(input('Informe se deseja continuar ou não [S/N]: ')).strip().upper()
    while pros not in 'SN':
        pros = str(input('Por gentileza, informe um input válido [S/N]: ')).strip().upper()
    if pros == 'N':
        if '5' in lista:
            print('O número 5 está presente na lista!')
        else:
            print('O número 5 não está presente na lista!')
        lista.sort(reverse=True)
        break
print(f'Foram digitados {cont} números e a lista ordenada de trás para frente é a seguinte: {lista}')