cont = 1
while True:
    n = int(input("Digite um numero positivo para saber a sua tabuada! "))
    if n < 0:
        break
    while cont <= 10:
        mul = n * cont
        print(f'{n} X {cont} = {mul}')
        cont += 1
    cont = 1    
print('fim')        
        
    