## Condições aninhadas

## if teste():
##     bloco 1
## elif teste2():
##     bloco 2
## elif teste3():
##     bloco 3
## else:
##     bloco 4

nome = str(input('Qual é o seu nome? '))

if nome == 'Hugo':
    print('Que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))