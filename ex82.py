lista1 =list()

while True:
    Valor = int(input('Digite um valor: '))
    lista1.append(Valor)
    
    opcao = input('Quer continuar?[S/N]').upper().strip()
    
    while opcao not in 'SN':
        print('Opção invalida!Digite uma valida!')
        opcao = input('Quer continuar?[S/N]').upper().strip()
        
    if opcao in 'N':
        break
    
listaPar = list()
listaImpar = list() 

for c in lista1:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)
        
print(f'A lista principal é {lista1}')

print(f'A lista de numeros pares é {listaPar}')

print(f'A lista de numeros impares é {listaImpar}')                  
    