tupla = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))

print(f'Você digitou os valores {tupla}')   

if 9 in tupla:
    print(f'O 9 foi digitado {tupla.count(9)} vezes!') 

else:    
    print('O numero 9 não foi digitado nenhuma vez!')    
    
if 3 in tupla:
    print(f'O numero 3 aparece na {tupla.index(3)+1}')    

else:    
    print('O numero 3 não foi digitado nenhuma vez!')        
    
    
print('Os numeros pares são:',end='')    
for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')