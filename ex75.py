tupla = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))

print(f'Você digitou os valores {tupla}')   

cont9 = 0

for c in tupla:
    
    if c == 9:
        cont9 += 1


if cont9 == 0:
    print('O numero 9 não foi digitado nenhuma vez!')    
    
else:
    print(f'O 9 foi digitado {cont9} vezes!')    
    
cont3 = 0

for c in tupla:
    
    if c == 3:
        cont3 += 1
        break
    
    elif c != 3:
        cont3 += 1

if cont3 == 0:
    print('O numero 3 não foi digitado nenhuma vez!')    
    
else:
    print(f'O 3 foi digitado na {cont3} posição!')    


contpares = 0

for c in tupla:
    
    if c % 2 == 0:
        contpares += 1

if contpares == 0:
    print('Não a numeros pares!')    
    
else:
    print(f'Tem {contpares} numeros pares!')    


                
    