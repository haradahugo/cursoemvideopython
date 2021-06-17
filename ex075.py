## Análise de dados em uma tupla
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite o último número: ')),)
if 3 in num:
    print(f'Você digitou os números {num}\nO número 9 apareceu {num.count(9)} vezes\nO número 3 foi digitado na {num.index(3)+1}ª posição \nOs números pares foram: ',end='')
    for par in num:
        if par % 2 == 0:
            print(par, end=' ')
else:
    print(f'Você digitou os números {num}\nO número 9 apareceu {num.count(9)} vezes\nO número 3 não foi digitado em nenhuma posição\nOs números pares foram: ',end='')
    for par in num:
        if par % 2 == 0:
            print(par, end=' ')
