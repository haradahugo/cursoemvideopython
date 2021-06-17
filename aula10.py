## CONDIÇÕES

nome = str(input('Qual é o seu nome? '))

if nome == 'Hugo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))

## CONDICIONAL EM UMA LINHA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))

print('Sua média foi boa! PARABÉNS!') if m>=6.0 else print('Sua média foi ruim! PRECISA MELHORAR!')