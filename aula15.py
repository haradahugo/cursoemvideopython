## Interrompendo repetições while

## While True executa o while para sempre, sendo quebrado pelo Break ou stopando o programa

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')