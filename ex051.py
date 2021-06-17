## Progressão Aritmética

inicial = int(input('Digite aqui o seu primeiro termo da PA: '))
razao = int(input('Digite aqui a razão da PA: '))

print('Para uma PA de primeiro termo {} e razão {} os dez primeiros valores são:\n'.format(inicial,razao))

for pa in range(inicial, inicial + 10 * razao, razao):
    print(pa)