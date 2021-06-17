## Alistamento Militar

from datetime import date

nasc = int(input('Digite aqui o seu ano de nascimento: '))
hoje = date.today().year

if hoje-nasc > 18:
    print('O seu tempo de se alistar já passou.\nVocê se alistou no ano de {}, já fazem {} anos!'.format(nasc+18, hoje-(nasc+18)))
elif hoje-nasc < 18:
    print('Você ainda se alistará para o exército. Isso será daqui {} anos, no ano de {}.'.format((nasc+18)-hoje, nasc+18))
elif hoje-nasc == 18:
    print('Este ano de {} você faz 18 anos, portato precisa se alistar!'.format(hoje))