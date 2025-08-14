print('-='*10)   
print('BANCO DO BRUM')
print('-='*10)

Valor = int(input("Digite um valor inteiro que queira sacar: R$"))
nota1 = nota10 = nota20 = nota50 = 0

while True:
    if Valor >= 50:
        nota50 += 1
        Valor -= 50
    
    elif Valor >= 20:
        nota20 += 1
        Valor -= 20
    
    elif Valor >= 10:
        nota10 += 1
        Valor -= 10
        
    elif Valor >= 1:
        nota1 += 1
        Valor -= 1
    
    elif Valor == 0:
        break

if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$50.')

if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20.')
    
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10.')

if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$1.')            

print('-='*10)
print("TENHA UM BOM DIA, VOLTE SEMPRE!")
           

   