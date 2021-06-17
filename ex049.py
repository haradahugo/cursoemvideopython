## Tabuada v2.0

tab = int(input('Digite aqui o número que você deseja ver a tabuada: '))

for ordem in range(0, 11):
    print('{} X {} = {}'.format(tab,ordem,tab*ordem))