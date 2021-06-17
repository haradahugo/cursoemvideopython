## Ler o nome de uma pessoa e dizer se possui "Silva" no nome

nome = str(input('Digite aqui o nome de uma pessoa: ')).strip()

print('O nome digitado foi \033[4;30;46m{}\033[m.\nE se o nome \033[31m"Silva"\033[m estiver presente o retorno será True, caso contrário será False: \033[1;32m{}\033[m'.format(nome, 'SILVA' in nome.upper()))