## Ler o nome da pessoa e mostrar qual é o primeiro e o último nome separadamente

nome = str(input('Digite aqui um nome: ')).strip().split()

print('O seu primeiro nome é: {}\nO seu último nome é: {}'.format(nome[0],nome[-1]))
