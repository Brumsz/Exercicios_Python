lista = list()

for c in range(0,5):
    valor = int(input("Digite um valor para a lista: "))
    
    if c == 0 or valor > lista[-1]:
        print(f'Adicionado no final da lista')
        lista.append(valor)
    
    else:
        cont = 0
        while cont < len(lista):
            if valor <= lista[cont]:
                lista.insert(cont,valor)
                print(f'Adicionado na posição {cont} da lista.')
                break
            cont += 1  


print(lista)        
        