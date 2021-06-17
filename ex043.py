## Índice de Massa Corporal

peso = float(input('Digite aqui o seu peso em Kg: '))
altura = float(input('Digite aqui a sua altura em metros: '))

imc = peso/(altura*altura)

if imc < 18.5:
    print('O seu IMC é de {:.1f}, este score é considerado como: Abaixo do Peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu IMC é de {:.1f}, este score é considerado como: Peso Ideal.'.format(imc))
elif 25 <= imc < 30:
    print('O seu IMC é de {:.1f}, este score é considerado como: Sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('O seu IMC é de {:.1f}, este score é considerado como: Obesidade.'.format(imc))
else:
    print('O seu IMC é de {:.1f}, este score é considerado como: Obesidade Mórbida.'.format(imc))