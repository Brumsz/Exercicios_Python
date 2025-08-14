import random
import time


print('-=-' * 20)
print('Mega Sena'.upper().center(50))
print('-=-' * 20)

jogos = int(input('Quantos jogos quer que eu faça? ')) 

print(f'Sorteando {jogos} jogos'.upper().center(50,'='))

for c in range (jogos):
    lista = random.sample(range(1,60),6)
    time.sleep(0.7)
    print(f'Jogo {c+1}: {lista}')

print('Boa Sorte!'.center(50,'=').upper())    
    
   