pessoas = list()
menorP = maiorP = 0


while True:
    #Nessa primeira parte estou adicionando valores compostos a lista pricipal pessoas
    nome = str(input("Insira um nome: "))
    peso = float(input("Insira o peso: "))
    
    lista = list()
    lista.append(nome)
    lista.append(peso)  
    
    pessoas.append(lista)
    
    #Verificação de resposta
    res = input('Quer continuar?[S/N]').upper().strip()
    while res not in 'SN':
         res = input('Resposta invalida!Digite uma opção valida![S/N]').upper().strip()
    
    if res == 'N':
        break

#Isso serve para ver qual é o menor e maior peso da lista    
for c in range(0,len(pessoas)):
    if c == 0:
        menorP = maiorP = pessoas[c][1] 
    
    elif maiorP < pessoas[c][1]:
        maiorP = pessoas[c][1]
    
    elif menorP > pessoas[c][1]:
        menorP = pessoas[c][1]    

#Aqui foi para printar o nome e peso dos mais leves e mais pesados.
print(f'O maior peso foi de {maiorP}KG. Peso de ',end ='')
for c in range(0,len(pessoas)):
    if pessoas[c][1] == maiorP:
        print(pessoas[c][0], end=' ')
        

print(f'\nO menor peso foi de {menorP}KG. Peso de ',end ='')
for c in range(0,len(pessoas)):
    if pessoas[c][1] == menorP:
        print(pessoas[c][0], end=' ')
                
        
    
           


     
        
            
    