## Lista ordenada sem repetições
lista = []
maior = menor = 0
for v in range(0,5):
    num = int(input('Informe o número que deseja incluir na lista: '))
    if v == 0:
        lista.append(num)
    if v == 1:
        if num > lista[0]:
            lista.insert(1,num)
        else:
            lista.insert(0,num)
    if v == 2:
        if num > lista[0]:
            if num > lista[1]:
                lista.insert(2,num)
            else:
                lista.insert(1,num)
        if num < lista[0]:
            lista.insert(0,num)
    if v == 3:
        if num < lista[0]:
            lista.insert(0,num)
        elif num > lista[2]:
            lista.insert(3,num)
        elif num > lista[0]:
            if num > lista[1]:
                lista.insert(2,num)
            if num < lista[1]:
                lista.insert(1,num)
    if v == 4:
        if num < lista[0]:
            lista.insert(0,num)
        elif num > lista[3]:
            lista.insert(4,num)
        elif num > lista[0]:
            if num < lista[1]:
                lista.insert(1,num)
            if num > lista[1]:
                if num < lista[2]:
                    lista.insert(2,num)
                if num > lista[2]:
                    lista.insert(3,num)
print(f'Segue lista de forma ordenada sem usar o sort(): {lista}')