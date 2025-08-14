#Nesse progama eu vou pedir para o usuario inserir 5 valores de peso para  pessoas, e então vou mostrar qual foi o menor peso
menor = 0
maior = 0
for c in range(0,5):
    pessoas =float(input("Coloque seu peso: "))
    if c == 1:
        menor = pessoas
        maior = pessoas 
    if pessoas < menor:
        menor = pessoas
    if pessoas > maior:
        maior = pessoas

print("o peso {} foi o menor".format(menor))        
print("o peso {} foi o maior".format(maior))    