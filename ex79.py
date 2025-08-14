lista = list()

while True:
    numero = int(input("Digite um valor: "))
    if numero in lista:
         print('Esse valor ja existe na lista! Digite um numero diferente!')
    else:
         lista.append(numero)
        
    opcao = input('Deseja continuar?[S/N]').upper().strip()
    while opcao not in 'SN':
        print("Opção invalida! Digite um valor valido!")
        opcao = input('Deseja continuar?[S/N]').upper().strip()
        
    if opcao in 'N':
        break

lista.sort()
print(f'Você digitou os valores {lista}')    
        
        
