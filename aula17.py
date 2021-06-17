## Diferente das tuplas, as listas podem ser mutáveis
comidas = ['Lanche','Suco','Pizza','Sorvete']
print(comidas)
comidas.append('Cookie') ##Adiciona Cookie na última posição da lista
print(comidas)
comidas.insert(0,'Cachorro quente') ##Adiciona Cachorro quente na posição zero da lista
print(comidas)

## Removendo a Pizza da lista
## del comidas[3]
## comidas.pop(3)  caso não dê parâmetro para o pop, o último elemento da lista é eliminado
## lanche.remove('Pizza')  elimina a primeira ocorrência dentro da lista
## Após a eliminação, os índices são atualizados
del comidas[3]
print(comidas)

## Criando listas com range
valores = list(range(4,11))
print(valores)

## Ordenando uma lista
ordem = [8,2,5,4,9,3,0]
print(ordem)
ordem.sort()
print(ordem)
ordem.sort(reverse=True)
print(ordem)
print(len(ordem))
ordem[3] = 7
print(ordem)

## Organizando o print
teste = []
teste.append(5)
teste.append(9)
teste.append(4)
for v in teste:
    print(f'{v}...',end = '')
for c, v in enumerate(teste):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

## Peculiaridade das listas
a = [2,3,4,7]
b = a  ## O Python faz uma ligação entre as listas, portanto, toda mudança feita em uma será replicada na outra. a=b não é uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
c = a[:]  ## Pega todos os valores de A e joga em C, criando uma cópia sem interligação entre listas
c[2] = 9
print(f'Lista A: {a}')
print(f'Lista C: {c}')