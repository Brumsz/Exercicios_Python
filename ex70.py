print('-='*10)
print('MERCADÃO')
print('-='*10)

total = maismil = cont = 0    
baratoN = ''
baratoP = 0


while True:
    nome = input("Nome do produto: ")
    preco = float(input('Digite o preço: R$'))
    
    total += preco
    cont += 1 
    
    if preco >= 1000:
        maismil += 1
    
    if cont == 1:
        baratoN = nome
        baratoP = preco
    
    elif preco < baratoP:
        baratoN = nome
        baratoP = preco
    
    continuar = input("Quer continuar?[S/N] ").upper().strip()[0]
    
    while continuar not in 'SsNn':
         continuar = input("Quer continuar?[S/N] ").upper().strip()[0]
    
    if continuar in 'Nn':
        break
    print('-='*10)   
print('-='*10)              

print(f'O total da compra foi de R${total}.')
print(f'{maismil} produto(s) custou mais de R$1000.')     
print(f'O produto mais barato foi {baratoN} custando R${baratoP}.')      
    
        