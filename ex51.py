
maior = 0
menor = 0
res = ' '
soma = 0
dig = 0

while res not in "Nn":  
    num = int(input("Digite um numero inteiro: "))
    soma += num
    dig += 1
    res = str(input("Deseja continuar? [S/N]"))    
    if res not in "NnSs":
        print("Digite uma resposta valida!")
        res = str(input("Deseja continuar? [S/N]"))

media = soma / dig

print("Você digitou {} numeros, e a media deles é de {:.1f} .".format(dig,media))        
       
            
    
    