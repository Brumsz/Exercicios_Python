expressao = input('Digite uma expressão: ')

lista = list(expressao)

cont = 0

for c in lista:
    if c in '()':
        cont += 1
        
if cont % 2 == 0:
    print('A expressão esta correta!')

else:
    print('A expressão está incorreta!')            

