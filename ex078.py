## Maior e menor valores na lista
valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite aqui um número inteiro na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Os valores informados foram: {valores}')
print(f'O maior valor informado foi {maior} nas posições ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor informado foi {menor} nas posições ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ',end='')
print()