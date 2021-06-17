## Sorteio de aluno
import random

n1 = str(input('Digite o primeiro aluno: '))
n2 = str(input('Digite o segundo aluno: '))
n3 = str(input('Digite o terceiro aluno: '))
n4 = str(input('Digite o quarto aluno: '))
lista = [n1, n2, n3, n4]

print('O aluno escolhido para apagar o quadro negro foi: {}!'.format(random.choices(lista)))