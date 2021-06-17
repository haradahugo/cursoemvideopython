## Lista composta e análise de dados
tempo = []
principal = []
pesados = leves = count = 0
while True:
    tempo.append(str(input('Nome: ')))
    tempo.append(float(input('Peso(Kg): ')))
    if len(principal) == 0:
        pesados = leves = tempo[1]
    else:
        if tempo[1] > pesados:
            pesados = tempo[1]
        if tempo[1] < leves:
            leves = tempo[1]
    principal.append(tempo[:])
    count += 1
    tempo.clear()
    follow = str(input('Deseja continuar com os cadastros? [S / N] ')).strip().upper()
    while follow not in 'SN':
        follow = str(input('Por gentileza, digite uma opção válida [S / N]: ')).strip().upper()
    if follow == 'N':
        break
print(f'Foram cadastradas {count} pessoas!')
print('Os mais pesados foram: ',end='')
for pessoas in principal:
    if pessoas[1] == pesados:
        print(f'[{pessoas[0]}]',end='')
print('\nOs mais leves foram: ',end='')
for pessoas in principal:
    if pessoas[1] == leves:
        print(f'[{pessoas[0]}]',end='')