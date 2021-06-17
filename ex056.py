## Analisador completo
soma = 0
cont = 0
maioridadehomem = 0
nomevelho = ''
mulheres = 0
for g in range(1,5):
    print('\n----- {} ª PESSOA -----'.format(g))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    cont += 1
    if g == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
media = soma / cont
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho possui {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))