## Grupo da maioridade

from datetime import date

p1 = int(input('Digite aqui o primeiro ano de nascimento: '))
p2 = int(input('Digite aqui o segundo ano de nascimento: '))
p3 = int(input('Digite aqui o terceiro ano de nascimento: '))
p4 = int(input('Digite aqui o quarto ano de nascimento: '))
p5 = int(input('Digite aqui o quinto ano de nascimento: '))
p6 = int(input('Digite aqui o sexto ano de nascimento: '))
p7 = int(input('Digite aqui o sétimo ano de nascimento: '))

lista = [p1,p2,p3,p4,p5,p6,p7]

maior = sum(1 for i in lista if date.today().year - i >=21)

print('{} pessoas já alcançaram a maior idade, {} ainda não.'.format(maior, 7-maior))