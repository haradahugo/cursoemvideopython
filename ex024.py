## Lendo nome de cidade e verificando se começa com o nome "Santo"

cidade = str(input('Digite aqui o nome de uma cidade: ')).split()

print('Se a cidade começar com \033[7m"Santo"\033[m em seu nome, aparecerá 0 caso contrário aparecerá -1: \033[1;31m{}\033[m'.format(cidade[0].find('Santo')))