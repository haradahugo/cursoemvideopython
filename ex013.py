## Salário e aumento
salario = float(input('Digite o valor do seu salário atual:'))
aumento = salario + (salario*0.15)
print('O valor do seu salário é de R${:.2f}.\nApós o seu aumento de 15% o valor será de R${:.2f}!!!'.format(salario,aumento))