
cont = soma = 0
print('Para parar o codigo use o numero 999!')

while True:
    n = int(input("Digite um valor inteiro: "))
    if n == 999:
        break
    cont += 1
    soma += n

print(f"Fora digitados {cont} numeros e a soma entre eles é {soma}")    