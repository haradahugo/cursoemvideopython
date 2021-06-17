## Criando um Menu de Opções

v1 = float(input('Informe o 1º valor: '))
v2 = float(input('Informe o 2º valor: '))
menu = int(input('\nSelecione uma das opções para o programa fazer o cálculo:\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]DIGITAR NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n'))
while menu > 5:
    menu = int(input('Por favor, digite uma opção válida: '))
while menu == 4:
    v1 = float(input('Informe o 1º valor: '))
    v2 = float(input('Informe o 2º valor: '))
    menu = int(input('\nSelecione uma das opções para o programa fazer o cálculo:\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]DIGITAR NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n'))
    menu = menu
    while menu > 5:
        menu = int(input('Por favor, digite uma opção válida: '))
if menu == 1:
    soma = v1 + v2
    print('A soma entre {:.1f} e {:.1f} resulta em {:.1f}.'.format(v1, v2, soma))
elif menu == 2:
    mult = v1 * v2
    print('A multiplicação entre {:.1f} e {:.1f} resulta em {:.1f}.'.format(v1, v2, mult))
elif menu == 3:
    maior = v1
    if maior < v2:
        print('O maior valor é {:.1f}.'.format(v2))
    else:
        print('O maior valor é {:.1f}'.format(v1))
elif menu == 5:
    print('Programa encerrado.')