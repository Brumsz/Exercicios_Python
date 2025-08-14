listatot =list()
dick = dict()
listaGols =list()
tot = 0
while True:
    dick['nome'] = str(input('Digite o nome do jogador: '))

    partidas = int(input(f'Quantas partidas {dick["nome"]} jogou? '))
    if partidas == 0:
        dick['Gols'] = 0     

    for c in range(partidas):
        gols = int(input(f'Gols na partida {c+1}: '))
        tot += gols
        listaGols.append(gols)
        

    dick['Gols'] = listaGols[:]
    dick['total'] = tot
    
    listatot.append(dick.copy())
    
    res = str(input('Quer continuar?[S/N]')).strip().upper()
    while res not in 'SN':
        res = str(input('Resposta invalida!Digite um valor valido.[S/N]'))
    
    if res in 'N':
        break    
    tot = 0
    listaGols.clear()
        
print('-=' * 20)
print('Cod',f'{'Nome':>5}',f'{'Gols':>10}',f'{'total':>12}')

cont = 0
for c in listatot:
    print([cont],f'{listatot[cont]["nome"]:>5}', f'{str(listatot[cont]["Gols"]):>10}',f'{listatot[cont]["total"]:>12}')
    cont += 1  
    

print('-'*40)

while True:
    dados = int(input('Mostrar dados de qual jogador,Escolha o numero deles estão na lista(999 para quebrar o código)'))
    
    while dados > len(listatot) and dados != 999:
        print('-'*40)
        dados = int(input('Dados invalidos!Escolha o numero deles estão na lista(999 para quebrar o código)'))
    if dados == 999:
        break
         
    print(f'Levantamento do Jogador {listatot[dados]["nome"]}'.center(20,'-'))
    if len(listatot[dados]["Gols"] ) > 0:  
        print('-'*40)       
        for c in range(len(listatot[dados]["Gols"])):
            print(f'No jogo {c+1} fez {listatot[dados]["Gols"][c]}.') 
    else:
        print('-'*40)  
        print(f'{listatot[dados]["nome"]} não tem jogos!')                 
    print('-'*40)       
print('-=' * 20)
print(f'Finalizado'.center(20,'-'))

