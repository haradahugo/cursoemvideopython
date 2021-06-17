## Números primos

num = int(input('Digite aqui um número para saber se ele é primo: '))

tot = 0

for intervalo in range(1, num+1):
    if num % intervalo == 0:              ##Mostra para quais números o num inputado é divisível
        print('\033[34m', end = '')
        tot = tot + 1                     ##Pode representar como tot += 1
    else:                                 ##Mostra para quais números o num inputado não é divisível
        print('\033[31m', end = '')
    print('{} '.format(intervalo))
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')