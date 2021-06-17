## Ordem do sorteio
import random

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
sorteio = random.shuffle(lista)
print('O sorteio foi feito e a ordem dos alunos para a apresentação foi: {}'.format(lista))