## Lendo números e mostrando suas unidades

num = int(input('Digite aqui um número qualquer entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('O número digitado foi \033[1;35m{}\033[m\nunidade: \033[32;40m{}\033[m\ndezena: \033[32;40m{}\033[m\ncentena:\033[32;40m{}\033[m\nmilhar: \033[32;40m{}\033[m'.format(num,u,d,c,m))