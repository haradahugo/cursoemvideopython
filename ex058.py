## Jogo da Adivinhação 2.0

from random import randint
from time import sleep

chances = 1

print('--*-- JOGO DA ADIVINHAÇÃO 2.0 --*--\n')
computador = randint(0,10)
print('ESTOU PENSANDO EM UM NÚMERO DE 0 A 10!')
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(1)
print('JÁ PENSEI!')
jogador = int(input('Digite aqui um número e veja se você acertou: '))

while jogador >= 11:
    jogador = int(input('O número digitado é inválido, por favor, tente novamente: '))
while jogador != computador:
    chances += 1
    print('\nOPS, parece que você errou!')
    tent = int(input('Tente novamente: '))
    jogador = tent
print('\nPARABÉNS!!!\nVOCÊ CONSEGUIU ACERTAR NA {}ª TENTATIVA(S)!\nEU PENSEI NO NÚMERO {}!'.format(chances,computador))