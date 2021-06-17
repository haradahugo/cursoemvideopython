## Detector de palíndromo

frase = str(input('Digite aqui uma frase e veja se ela é um palíndromo: ')).strip().lower().replace(' ','')

if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')