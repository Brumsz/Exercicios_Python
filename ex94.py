dick = dict()
lista = list()

while True:
    dick['Nome'] = str(input('Digite o nome: '))
    dick['idade'] = int(input('Digite a idade: '))
    dick['Sexo'] = str(input('Digite o sexo[M/F]: ')).strip().upper()
    while dick['Sexo'] not in 'FM':
        dick['Sexo'] = str(input('Digite um sexo valido![M/F]: ')).strip().upper()
        
    
    lista.append(dick.copy())
    
    res = str(input('Deseja continuar?[S/N]')).strip().upper()
    while res not in 'SN':
        res = str(input('Valor invalido!Insira um valor certo![S/N]')).strip().upper()
    
    if res in 'N':
        break

print('-=' * 20)

idade = 0

for c in range(len(lista)):
    idade += lista[c]["idade"]       
    
media = idade // len(lista) 

print(f"- O grupo tem {len(lista)} pessoas")
print(f'- A média de idade é {media}')

print(f'- As mulheres cadastradas foram: ',end='')
for c in range(len(lista)):
    if lista[c]["Sexo"] in 'F':
        print(f'{lista[c]["Nome"]}',end=' ')
print()
print('- Lista das pessoas com idade acima da média: ') 
for c in lista:
    if c["idade"] > media:
        print('   ')
        for k,v in c.items():
            print(f'{k} = {v};',end='')
        print()    

print('-='*7,'FIM','-='*7)        
        