## Variáveis Compostas - Tuplas
## Tuplas armezanam mais de um valor em uma só variável
## As tuplas são IMUTÁVEIS, não há como eliminar/adicionar elementos numa tupla
## Tuplas aceitam int, float, str etc
lanche = ('Hambúrguer','Suco','Pizza','Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[:2])
print(sorted(lanche)) ##Ordem alfabética
for cont in range(0,len(lanche)):
    print(lanche[cont])
## lanche[1] = 'Refrigerante' Dá erro ao tentar atribuir novos elementos a uma tupla
teste = 'Coca','Sprite','Guaraná'    ##Também é uma tupla, só que sem o uso dos ()
for bebidas in teste:
    print(f'Eu vou beber {bebidas}')
print(teste[1])
print(teste[:2])
for pos,bebidas in enumerate(teste):
    print(f'Eu vou beber {bebidas}, na posição {pos}')

a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(c.count(5))
print(c.index(8))