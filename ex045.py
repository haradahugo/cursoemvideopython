## GAME: Pedra, papel e tesoura

from random import randrange,randint
from time import sleep

player = int(input('VAMOS JOGAR JOKENPÔ!\n\nFaça sua escolha:\n[ 0 ]PEDRA\n[ 1 ]PAPEL\n[ 2 ]TESOURA\n'))
pc = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')

if player == pc:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nDEU EMPATE, DEU VÉIAAA!'.format(itens[player],itens[pc]))
elif player == 0 and pc == 1:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nEU GANHEI!!! HA HA HA HUMANO BOBO.'.format(itens[player],itens[pc]))
elif player == 0 and pc == 2:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nVocê ganhou...'.format(itens[player],itens[pc]))
elif player == 1 and pc == 0:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nVocê ganhou...'.format(itens[player],itens[pc]))
elif player == 1 and pc == 2:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nEU GANHEI!!! HA HA HA HUMANO BOBO.'.format(itens[player],itens[pc]))
elif player == 2 and pc == 0:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nEU GANHEI!!! HA HA HA HUMANO BOBO.'.format(itens[player],itens[pc]))
elif player == 2 and pc == 1:
    print('PROCESSANDO...')
    sleep(2)
    print('Jogador: {}\nComputador: {}\nVocê ganhou...'.format(itens[player],itens[pc]))
else:
    print('Digite um valor válido.')