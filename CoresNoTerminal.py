## Cores no Terminal

## \033[STYLE;TEXT;BACKm formatação para cores no terminal Python
## Style: 0(none), 1(bold), 4(underline) ou 7(negative)
## Text: 30(white), 31(red), 32(green), 33(yellow), 34(blue), 35(magenta), 36(light blue) ou 37(grey - default)
## Back: 40(white), 41(red), 42(green), 43(yellow), 44(blue), 45(magenta), 46(light blue) ou 47(grey - default)

print('\033[7mOlá, Mundo!\033[m')

a=3
b=5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Hugo'

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[36;4m', nome, '\033[m'))