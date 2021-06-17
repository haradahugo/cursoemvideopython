## Aprovando empréstimo

casa = float(input('Digite aqui o valor da casa a se comprar: '))
sal = float(input('Digite aqui o valor do seu salário mensal: '))
anos = int(input('Digite aqui em quantos anos a casa será paga: '))

meses = anos*12
prest = casa/meses

if prest > sal*0.3:
    print('O valor da prestação mensal a ser paga é de \033[31mR${:.2f}\033[m e excede em 30% o valor do seu salário que é de \033[31mR${:.2f}\033[m, portanto o empréstimo será negado.'.format(prest,sal*0.3))
else:
    print('O valor da prestação mensal a ser paga é de \033[31mR${:.2f}\033[m e com sua margem de 30% do seu salário que é de \033[32mR${:.2f}\033[m, está dentro dos critérios de aprovação do empréstimo!\nO seu empréstimo será concedido!!!'.format(prest,sal*0.3))