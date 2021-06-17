## Aquele Clássico da Média

n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite aqui a sua segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print('Sua média foi de \033[31m{}\033[m, ou seja, abaixo de 5.0: \033[31mREPROVADO\033[m!'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média foi de \033[33m{}\033[m, ou seja, entre 5.0 e 6.9: \033[33mRECUPERAÇÃO\033[m!'.format(media))
elif media >= 7.0:
    print('Sua média foi de \033[32m{}\033[m, ou seja, maior ou igual a 7.0: \033[32mAPROVADO\033[m!'.format(media))