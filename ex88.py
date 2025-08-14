lista =list()

while True:
    nome = input('Insira o nome do aluno: ')
    
    nota1 = float(input('Digite a primeira nota: '))
    while nota1 > 10:
        nota1 = float(input('Sua nota não pode ser maior que 10,digite uma nota valida: '))
    
    nota2 = float(input('Digite a segunda nota: '))
    while nota2 > 10:
        nota2 = float(input('Sua nota não pode ser maior que 10,digite uma nota valida: '))
    
    aluno = list()
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    
    lista.append(aluno[:])
    
    res = input('Quer continuar? [S/N] ').upper().strip()
    while res not in 'SN':
         res = input('Resposta invalida!Digite uma opção valida![S/N]').upper().strip()
    
    if res == 'N':
        break

print('-=' * 20)

print('NO.',end='')
print('Nome'.center(13),end='')
print('Média'.center(20))    
print('-' * 40 )


for c in range(len(lista)):
    media = (lista[c][1] + lista[c][2]) / 2    
    print(f'{c}',end='')
    print(f'{lista[c][0]}'.center(17),end='')
    print(f'{media}'.center(15))
    
print('-' * 40 )    

while True:
    resposta=int(input('Mostrar nota de qual aluno?(999 interrompe)'))
    
    c = len(lista)
    if resposta == 999:
        break    
    while resposta >= c:
         resposta=int(input('Aluno não encontrado!Insira um numero valido(999 interrompe)'))
    
    print(f'As notas de {lista[resposta][0]} são {lista[resposta][1]} e {lista[resposta][2]}')
    
     

print('FINALIZADO'.center(50,'-'))    
    
    