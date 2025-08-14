lista = list()

while True:
    n = int(input('Digite um valor para colocar na lista: '))
    lista.append(n)
    
    opcao =input('Deseja continuar?[S/N]').upper().strip()
    
    while opcao not in 'SN':
        print('Opção invalida!Digite novamente!')
        opcao =input('Deseja continuar?[S/N]').upper().strip()
    
    if opcao in 'N':
        break


print(f'Nessa lista foram digitados {len(lista)} caracteres!')            

lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é {lista}')

cont = 0
for c in lista:
    if c == 5:
        break
    else:
        cont += 1
    
    
if 5 in lista:
    print(f'Existe o numero 5 na lista!E se encontra na posição {cont}!')

else:
    print('Não existe o numero 5 na lista!')    
            