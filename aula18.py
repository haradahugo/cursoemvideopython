## Listas dentro de listas
dados = list()
dados.append("Hugo")
dados.append(22)
pessoas = list()
pessoas.append(dados[:])
print(dados)
print(pessoas)
gente = [['Pedro',25],['Duda',19],['João',32]]
print(gente[0][0])
print(gente[1])

## Prática
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
grupo = []
dados = []
for d in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    grupo.append(dados[:])
    dados.clear()
print(grupo)
totmai = totmen = 0
for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')