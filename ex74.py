from random import randint

numeros = tuple(randint (0,100) for c in range(5))

print(f'Os numeros escolidos foram {numeros}')


print(f'O menor numero é {min(numeros)}')
print(f'O maior numero é {max(numeros)}')         

        
    
    
    