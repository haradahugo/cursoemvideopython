## Validando expressões matemáticas
expr = str(input('Digite a expressão matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #Retira o último elemento da lista pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Suas expressão está errada!')