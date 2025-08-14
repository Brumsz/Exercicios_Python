num = int(input("Digite um numero inteiro para saber sua sequencia de fibonacci: "))
numant= num 

cont = 7

while cont != 0:
    num = num + numant
    cont -= 1
    print("{}->".format(num))  