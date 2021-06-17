## Tamanho da parede e quantidade de tinta
# Cada litro de tinta pinta uma área de 2m². Qual o tamanho da parede e qual a quantidade de tinta necessária para pintá-la?
l = float(input('Digite o valor da largura de sua parede:'))
a = float(input('Digite o valor da altura de sua parede:'))
area = l * a
tinta = area/2
print('A área de sua parede é de {:.2f} m².\nA quantidade de tinta necessária para pintá-la é de {:.2f} l.'.format(area,tinta))