## Ler uma frase e mostrar quantas letras "A" ela possui, qual sua posição na primeira e última posição na frase
import unidecode

frase = str(input('Digite aqui qualquer frase: ')).lower().strip()
frasenaoacentuada = unidecode.unidecode(frase)

a = frasenaoacentuada.count('a')

first = frasenaoacentuada.find('a')+1

last = frasenaoacentuada.rfind('a')+1

print('A frase digitada possui {} letras A.\nA primeira posição em que ela aparece é {}.\nE a sua última aparição é em {}.'.format(a, first, last))