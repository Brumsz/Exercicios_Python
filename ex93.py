dick = dict()
listaGols =list()
tot = 0

dick['nome'] = str(input('Digite o nome do jogador: '))

partidas = int(input(f'Quantas partidas {dick["nome"]} jogou? '))

for c in range(partidas):
    gols = int(input(f'Gols na partida {c+1}: '))
    tot += gols
    listaGols.append(gols)
    

dick['Gols'] = listaGols
dick['total'] = tot

print('-=' * 20)
print(dick)
print('-=' * 20)

for k,v in dick.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 20)
print(f'O jogador {dick["nome"]} jogou {partidas} partidas.')
for c in range(partidas):
    print(f'=> Na partida {c+1} ele fez {dick["Gols"][c]}.')
print(f'Foram {dick["total"]} gols no total!')    