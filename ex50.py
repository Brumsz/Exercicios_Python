num = int(input("Digite um numero inteiro de 1 a 998, pois o numero 999 sera usado para fechar o progama: "))
dig = 0
soma = 0


while num != 999:
    if num != 999:
        dig += 1
        soma += num
    num = int(input("Digite um numero inteiro de 1 a 998, pois o numero 999 sera usado para fechar o progama: "))

print("Foram digitados {} numeros, e a soma deles sera {} .".format(dig,soma))    