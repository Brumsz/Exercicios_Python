aluno = {'Nome':str(input('Insira o nome: '))}
aluno['media'] = float(input(f'A média de {aluno["Nome"]}: '))

for k,v in aluno.items():
    print(f'{k} é igual a {v}!')

if aluno["media"] < 7:
    print(f'{aluno["Nome"]} esta reprovado!')
elif aluno["media"] > 10:
    print('Não tem com sua média ser essa, pare de brincar!')
    
else:        
    print(f'{aluno["Nome"]} esta aprovado!')