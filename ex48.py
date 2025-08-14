num =int(input("Digite um numero inteiro para saber o seu fatorial: "))
fat = num - 1
cont = 0
res = num

while fat != 0: 
    cont = res * fat
    res = cont
    fat -= 1

print("O resultado da faturação de {} é igual a {}".format(num,res))    