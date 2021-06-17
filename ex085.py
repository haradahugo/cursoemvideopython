## Listas com pares e ímpares
inter = []
for i in range(2):
    inter.append([])
for n in range(0,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0: #Lista dos pares
        inter[0].append(num)
    else: #Lista dos ímpares
        inter[1].append(num)
inter[0].sort()
inter[1].sort()
print(f'Os números pares digitados foram {inter[0]}\nOs número ímpares digitados foram {inter[1]}')