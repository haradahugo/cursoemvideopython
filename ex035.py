## Analisando Triângulo v1.0

print('Vamos verificar se três valores dados podem formar um triângulo!')

a = float(input('Digite aqui o valor do primeiro lado do triângulo: '))
b = float(input('Digite aqui o valor do segundo lado do triângulo: '))
c = float(input('Digite aqui o valor do terceiro lado do triângulo: '))

if abs(b-c) < a < b+c or abs(a-c) < b < a+c or abs(a-b) < c < a+b:
    print('É possível obter um triângulo a partir destes três números: {}, {} e {}.'.format(a,b,c))
else:
    print('Não é possível obter um triângulo a partir destes três números: {}, {} e {}.'.format(a,b,c))