lista = list()
maior = 0
menor = 0

for c in range(0,5):
    lista.append(int(input("Digite um valor: ")))
    

print(f'Você digitou {lista}')    

for c,v in enumerate(lista):
    
    if c == 0:
        maior = v
        menor = v
    
    elif v > maior:
        maior = v  
    
    elif v < menor:
        menor = v

print(f'O maior valor digitado foi {maior} nas posições: ',end ='')
for c,v in enumerate(lista):
    if v == maior:
        print(f'{c}',end = '...')


print(f'\nO menor numero digitado foi {menor} nas posições: ',end='')
for c,v in enumerate(lista):
    if v == menor:
        print(f'{c}',end='...')
          