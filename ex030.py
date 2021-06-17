## Par ou ímpar?

from time import sleep

num = int(input('Digite aqui um número inteiro aleatório: '))

if num % 2 == 0:
    print('Bip Bop, estou processando.')
    sleep(2)
    print('O número digitado é PAR!!!')
else:
    print('Bip Bop, estou processando.')
    sleep(2)
    print('O número digitado é ÍMPAR!!!')