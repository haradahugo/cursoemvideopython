## Custo da Viagem

dist = float(input('Digite aqui a distância em Km da sua viagem: '))

print('O preço da passagem para a distância de {}Km é de R${:.2f}.'.format(dist, dist*0.5)) if dist<=200 else print('O preço da passagem para a distância de {}Km é de R${:.2f}.'.format(dist, dist*0.45))