## Comparando Números

int1 = int(input('Digite aqui um número inteiro qualquer: '))
int2 = int(input('Digite aqui outro número inteiro qualquer: '))

if int1 > int2:
    print('O \033[36mprimeiro\033[m valor é maior!')
elif int2 > int1:
    print('O \033[36msegundo\033[m valor é maior!')
else:
    print('Não existe valor maior, os dois são \033[36miguais\033[m!')