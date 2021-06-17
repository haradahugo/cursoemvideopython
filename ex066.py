## Vário números com flag

n = s = c = 0

while True:
    n = int(input('Digite aqui um número inteiro ou 999 para parar: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} número e a soma de todos é de {s}.')