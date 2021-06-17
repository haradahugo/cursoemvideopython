## Gerenciador de Pagamentos

val = float(input('Digite aqui o valor a ser pago por um produto: '))
cond = int(input('Selecione e digite a sua opção de pagamento:\n1)À vista no dinheiro/cheque.\n2)À vista no cartão.\n3)Em até 2x no cartão.\n4)3x ou mais no cartão.\n'))

if cond == 1:
    avdin = val - (val*0.1)
    print('À vista no dinheiro ou cheque.\nValor a ser pago de R${:.2f}.'.format(avdin))
elif cond == 2:
    avcc = val - (val*0.05)
    print('Àvista no cartão.\nValor a ser pago de R${:.2f}.'.format(avcc))
elif cond == 3:
    cctwo = val
    print('Em até 2x no cartão.\nValor total a ser pago de R${:.2f} em 2 prestações de R${:.2f}.'.format(cctwo,(cctwo/2)))
elif cond == 4:
    ccplus = val + (val*0.2)
    parc = int(input('Digite aqui a quantidade de parcelas a serem pagas: '))
    parcval = ccplus / parc
    print('3x ou mais no cartão.\nValor total a ser pago de R${:.2f}, em {} parcelas de R${:.2f}.'.format(ccplus,parc,parcval))
else:
    print('Volte e selecione um método de pagamento válido!')