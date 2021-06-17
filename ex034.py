## Aumentos Múltiplos

sal = float(input('Digite aqui o valor do seu salário e veja quanto você receberá após o aumento: '))

if sal<=1250.00:
    print('O seu salário é de R${:.2f}, e após o aumento será de R${:.2f}.'.format(sal, (sal+(sal*0.15))))
else:
    print('O seu salário é de R${:.2f}, e após o aumento será de R${:.2f}.'.format(sal, (sal+(sal*0.1))))