## Análise de dados do grupo
cont_homens = cont_mulheres = cont_idade = 0
while True:
    sexo = str(input('Qual o sexo da pessoa? [F / M] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Por favor, digite novamente: ')).strip().upper()
    idade = int(input('Qual a idade da pessoa? '))
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1
    cont = str(input('Pessoa cadastrada com sucesso, deseja continuar? [S / N]? \n')).upper()
    while cont not in 'SN':
        cont = str(input('Por favor, digite uma entrada válida: ')).split().upper()
    if cont == 'N':
        break
print(f'{cont_idade} pessoas possuem mais de 18 anos.\n{cont_homens} homens foram cadastrados.\n{cont_mulheres} mulheres com menos de 20 anos foram cadastradas.')