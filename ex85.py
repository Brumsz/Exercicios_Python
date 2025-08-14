numeros = [[],[]]

for c in range(7):
    n = int(input("Digite um numero: "))
    
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros.sort()
print(f'Os valores pares digitados foram {numeros[0]}')  
print(f'Os valores impares digitados foram {numeros[1]}') 