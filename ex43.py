menor = 0
maior = 0
for c in range(0,7):
    pessoa = int(input("Digite sua idade: "))
    if pessoa >= 18:
        maior += 1
    else:
        menor += 1
print("Foi encontrado {} menores de idade".format(menor))
print("Foi encontrado {} maiores de idade".format(maior))            
        