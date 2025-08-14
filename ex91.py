import random

dicionario = dict()

for c in range(0,4):
    n = random.sample(range(0,6),1)   
    print(f'O jogador{c+1} tirou {n}')
    dicionario[f'jogador{c+1}'] = n



     


print(dicionario)    