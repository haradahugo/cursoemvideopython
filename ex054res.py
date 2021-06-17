from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(1,8):
    p = int(input('Digite aqui o {}º ano de nascimento: '.format(i)))
    idade = atual - p
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas já alcançaram a maior idade.\n{} ainda não alcançaram a maior idade.'.format(maior,menor))