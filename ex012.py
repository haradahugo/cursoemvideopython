## Preço e desconto
preco = float(input('Digite aqui o preço do produto desejado:'))
desconto = preco - (preco*0.05)
print('O valor digitado foi de R${:.2f}.\nO valor com desconto de 5% é de R${:.2f}.'.format(preco,desconto))