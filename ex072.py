## Número por extenso
extenso = 'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
num = int(input('Digite um número entre 0 e 20 para visualizá-lo por extenso: '))
while num > 20 or num < 0:
    num = int(input('Digite uma entrada válida: '))
print(f'Você digitou o número {extenso[num]}!')