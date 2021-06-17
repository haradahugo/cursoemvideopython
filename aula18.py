## Listas dentro de listas
dados = list()
dados.append("Hugo")
dados.append(22)
pessoas = list()
pessoas.append(dados[:])
print(dados)
print(pessoas)

