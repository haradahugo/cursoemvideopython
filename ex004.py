## Dissecando uma variável
msg = input('Digite algo: ')
type(msg)
print('O tipo primitivo desse valor é {}'.format(type(msg)))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um número? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alfanumérico? {}'.format(msg.isalnum()))
print('Está em maúsculas? {}'.format(msg.isupper()))
print('Está em minúsculas? {}'.format(msg.islower()))
print('Está capitalizada? {}'.format(msg.istitle()))