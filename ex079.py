## Valores únicos em uma lista
lista = []
cont = 0
while True:
    val = int(input('Digite aqui um número inteiro para ser adicionado à lista: '))
    if cont == 0:
        lista.append(val)
        print('Valor adicionado com sucesso...')
    if cont != 0:
        if val in lista:
            print(f'O número {val} já está na lista!')
        if val not in lista:
            lista.append(val)
            print('Valor adicionado com sucesso...')
    cont += 1
    lista.sort()
    seguir = str(input('Informe se deseja seguir ou não [S/N]: ')).strip().upper()
    while seguir not in 'SN':
        seguir = str(input('Por gentileza, informe um input válido [S/N]: ')).strip().upper()
    if seguir == 'N':
        break
print(f'Você digitou os valores {lista}')