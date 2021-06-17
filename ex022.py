## Lendo e analisando nomes
nome = str(input('Digite aqui o seu \033[31mnome completo\033[m: ')).strip()

print('O nome com todas as letras maiúsculas é: {}'.format(nome.upper()))

print('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))

print('A quantidade totais de letras do nome é: {}'.format(len(nome)-nome.count(' ')))

print('A quantidade de letras do primeiro nome é: {}'.format(nome.find(' ')))