lista = list()
posições = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

for c in range(9):
    n = int(input(f'Digite um valor para {posições[c]}: '))
    lista.append(n)

pares = somaC3 = maiorS2 = 0


for c in range(len(lista)):
    if lista[c] % 2 == 0:
        pares += lista[c]
        
for c in range(len(lista)):
    if c > 5:
        somaC3 += lista[c]
    
for c in range(len(lista)):
    if c > 2 and  c <= 5:
        if c > 3:
            maiorS2 = lista[c]
        elif maiorS2 < lista[c]:
            maiorS2 = lista[c]    
     

print('-=' * 40)
print(lista[0],lista[1],lista[2],'\n',
      lista[3],lista[4],lista[5],'\n',
      lista[6],lista[7],lista[8]
      )
print('-=' * 40)

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {somaC3}.')
print(f'O maior valor da segunda coluna é {maiorS2}.')
