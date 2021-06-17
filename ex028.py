## Jogo da Adivinhação

import random

print('Hmmm estou pensando em um número entre 0 e 5.\nTente adivinhar qual número eu escolhi!')

num = random.randrange(0,5)

user = int(input('Digite aqui o número que você acha que eu escolhi: '))
print('Hmmm você escolheu o número {}...'.format(user))

if num == user:
    print('Parabéns!!! Você acertou, eu escolhi o número {}.'.format(num))
else:
    print('Não foi desta vez que você adivinhou! Eu escolhi o número {}.'.format(num))