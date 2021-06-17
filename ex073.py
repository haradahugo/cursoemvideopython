## Tuplas com times de futebol
times = 'Flamengo','Internacional','Atlético Mineiro','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Athletico Paranaense','Red Bull Bragantino','Ceará','Corinthians','Atlético Goianiense','Bahia','Sport','Fortaleza','Vasco da Gama','Goiás','Coritiba','Botafogo'
print('CLASSIFICAÇÃO BRASILEIRÃO 2020')
print(f'Os cinco primeiros colocados foram: {times[:6]}')
print('*-'*60)
print(f'Os últimos quatro colocados foram {times[-4:]}')
print('*-'*60)
print(f'Os times em ordem alfabética são {sorted(times)}')
print('*-'*60)
for pos, clubes in enumerate(times):
    if clubes == 'Ceará':
        print(f'O {clubes} terminou em {pos+1}º lugar')