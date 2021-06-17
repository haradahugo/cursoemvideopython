## Jogo do Par ou Ímpar
from random import randint
c = 0
while True:
    print('\nVAMOS JOGAR PAR OU ÍMPAR!')
    computador = randint(0, 10)
    player = int(input('Digite aqui um número inteiro: '))
    esc = str(input('Você escolher par ou ímpar [P / I]? ')).upper()
    s = player + computador
    if esc == 'P' and s % 2 == 0:
        print(f'PARABÉNS, VOCÊ VENCEU!!!\nVocê jogou {player} e o computador {computador}, resultando em um número par!')
    if esc == 'I' and s % 2 != 0:
        print(f'PARABÉNS, VOCÊ VENCEU!!!\nVocê jogou {player} e o computador {computador}, resultando em um número ímpar!')
    if esc == 'P' and s % 2 != 0:
        print(f'VOCÊ PERDEU!!!\nVocê jogou {player} e o computador {computador}, resultando em um número ímpar!\nForam {c} vitórias consecutivas!')
        break
    if esc == 'I' and s % 2 == 0:
        print(f'VOCÊ PERDEU!!!\nVocê jogou {player} e o computador {computador}, resultando em um número par!\nForam {c} vitórias consecutivas!')
        break
    c += 1