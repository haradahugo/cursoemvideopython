## Classificando Atletas

from datetime import date

nasc = int(input('Digite aqui o seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - nasc

if idade <= 9:
    print('Sua idade é de {} anos, se encaixando na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('Sua idade é de {} anos, se encaixando na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('Sua idade é de {} anos, se encaixando na categoria JUNIOR!'.format(idade))
elif idade <= 25:
    print('Sua idade é de {} anos, se encaixando na categoria SÊNIOR!'.format(idade))
else:
    print('Sua idade é de {} anos, se encaixando na categoria MASTER!'.format(idade))