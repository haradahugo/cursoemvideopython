## Conversão BRL USD
real = float(input('Digite um valor e BRL e descubra quantos dólares você poderia comprar:'))
dolar = float(real/5.62) #cotação de 16/03/2021
print('Com R${:.2f} você poderia comprar US${:.2f}.'.format(real,dolar))