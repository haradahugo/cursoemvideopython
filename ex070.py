## Estatística em produtos
print('PYTHON CAIXA, SEJA BEM VINDO!')
total = 0
mil = 0
c = 0
while True:
    prod = str(input('Qual o produto? '))
    preco = float(input('Qual o preço? '))
    total += preco
    c += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = prod
    if preco > 1000:
        mil += 1
    cont = str(input('Deseja continuar? [S / N] \n')).upper()
    if cont == 'N':
        break
    while cont not in 'S':
        cont = str(input('Deseja continuar? [S / N] \n')).upper()
print(f'Valor total da compra: R${total:.2f}\n{mil} produtos acima de R$1000.00\nO produto mais barato foi {barato} que custa R${menor:.2f}')