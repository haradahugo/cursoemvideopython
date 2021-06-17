## Radar Eletrônico

km = float(input('Digite aqui a velocidade em Km/h de um carro: '))

print('Pela velocidade informada de {}Km/h, a multa a ser paga é de R${:.2f}.'.format(km, ((km-80)*7))) if km>=80 else print("A velocidade informada de {}Km/h está dentro do limite de velocidade!".format(km))