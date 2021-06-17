## Tabuada v3.0

while True:
    tab = int(input('Digite um número inteiro para ver sua tabuada, ou um negativo para parar: '))
    if tab < 0:
        break
    print(f'1 X {tab} = {tab*1}\n2 X {tab} = {tab*2}\n3 X {tab} = {tab*3}\n4 X {tab} = {tab*4}\n5 X {tab} = {tab*5}\n6 X {tab} = {tab*6}\n7 X {tab} = {tab*7}\n8 X {tab} = {tab*8}\n9 X {tab} = {tab*9}\n10 X {tab} = {tab*10}')
print('O valor digitado foi negativo! Obrigado por usar a tabuada e volte sempre!')