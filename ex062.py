## Super Progressão Aritmética v3.0
a1 = int(input('Digite aqui o primeiro termo: '))
r = int(input('Digite aqui a razão: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end = '')
        termo += r
        cont += 1
    print('...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))