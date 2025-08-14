import datetime

dick = dict()

dick['Nome'] = str(input('Insira seu nome: '))

#idade
nasc = int(input('Insira seu ano de nascimento: '))
dick['idade'] =  datetime.datetime.now().year - nasc 

dick['ctps'] = int(input('Carteira de trabalho(0 não tem)'))

if dick['ctps'] == 0:
    print('-=' * 20)
    print(dick)
    for k,v in dick.items():
        print(f'{k} tem valor de {v}')

else:
    
    dick['contratação'] = int(input('Ano da contratação: '))
    dick['salario'] = float(input('Salario: R$'))
    
    aposentadoria = (dick['contratação'] + 35) - nasc 
    dick['aposentadoria'] = aposentadoria
    
    print('-=' * 20)
    print(dick)
    for k,v in dick.items():
        print(f'{k} tem valor de {v}')
    
