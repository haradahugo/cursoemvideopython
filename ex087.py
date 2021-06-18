## Mais sobre Matriz em Python
print('Matriz 3 x 3 em Python')
matriz = list()
soma = maior = 0
for m in range(1,10):
    num = (int(input(f'Digite um valor para a posição {m}: ')))
    matriz.append(num)
    if num % 2 == 0:
        soma += num
    if 4 <= m <= 6:
        if m == 4:
            maior = matriz[3]
        elif m == 5 and maior < matriz[4]:
            maior = matriz[4]
        elif m == 6 and maior < matriz[5]:
            maior = matriz[5]
print('*-'*9)
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')
print(f'A soma de todos os valores pares digitados foi de {soma}.')
print(f'A soma dos valores da terceira coluna foi de {matriz[2]+matriz[5]+matriz[8]}.')
print(f'O maior valor da segunda linha foi o {maior}.')
