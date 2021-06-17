## Contagem regressiva

from time import sleep

for fogos in range(10,-1,-1):
    print('Faltam {} segundos!'.format(fogos))
    sleep(1)
print('FELIZ ANO NOVO!!!')