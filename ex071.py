## Simulador de Caixa Eletrônico
## Notas disponíveis: R$50, R$20, R$10 e R$1

saque = int(input('Informe aqui o valor a ser sacado: R$'))
total = saque
cont_cinq = 0
cont_vinte = 0
cont_dez = 0
cont_um = 0

while True:
    if saque % 50 == 0:
        cont_cinq += saque // 50
        saque = saque % 50
        total = total - (cont_cinq * 50)
    elif saque % 20 == 0:
        cont_vinte += saque // 20
        saque = saque % 20
        total = total - (cont_vinte * 50)
    elif saque % 10 == 0:
        cont_dez += saque // 10
        saque = saque % 10
        total = total - (cont_dez * 10)
    elif saque % 1 == 0:
        cont_um += saque // 1
        saque = saque % 1
        total = total - (cont_um * 1)
    if saque == 0:
        break
print(f'Total de {cont_cinq} cédulas de R$50,00\nTotal de {cont_vinte} cédulas de R$20,00\nTotal de {cont_dez} cédulas de R$10,00\nTotal de {cont_um} cédulas de R$1,00')