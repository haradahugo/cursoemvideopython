## Aluguel de carros
#Custo do carro alugado: R$60,00 por dia e R$0,15 por Km rodado.,
periodo = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
custo = (periodo*60)+(km*0.15)
print('O carro foi alugado por {} dias e rodou {:.2f} Km.\nO custo total para foi de R${:.2f}.'.format(periodo,km,custo))