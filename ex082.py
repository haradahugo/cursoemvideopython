## Dividindo valores em várias listas
original = []
par = []
impar = []
while True:
    num = int(input('Digite aqui um número inteiro: '))
    original.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continua = str(input('Informe se deseja continuar [S/N]: ')).strip().upper()
    while continua not in 'SN':
        continua = str(input('Por gentileza, dê um input válido [S/N]: ')).strip().upper()
    if continua == 'N':
        original.sort()
        par.sort()
        impar.sort()
        break
print(f'Seguem as listas geradas e ordenadas de forma crescente:\nLista com todos os valores: {original}\nLista com os valores pares: {par}\nLista com os valores ímpares: {impar}')