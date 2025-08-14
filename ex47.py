v1 =int(input('Digite um numero inteiro: '))
v2 =int(input('Digite outro numero inteiro: '))


print('================================\n ESCOLHA DE OPERAÇÕES \n [1]SOMAR \n [2]MULTIPLICAR \n [3]MAIOR \n [4]NOVOS NUMEROS \n [5]SAIR DO PROGAMA \n================================')

caso =int(input('SELECIONE UMA DAS OPÇÕES: '))


while caso != 5:
        if caso == 1:
            print('Você escolheu a soma: ', v1 + v2)
        if caso == 2:
            print('Você escolheu mutiplicar: ', v1 * v2)
        if caso == 3:
            if v1 > v2:
                print('Você quer saber qual valor é o maior, o maior é: ',v1)
            if v1 < v2:
                print('Você quer saber qual valor é o maior, o maior é: ',v2)
            else:
                print('Você quer saber qual valor é o maior, porem os dois possuem o mesmo valor')  
        if caso == 4:
            v1 =int(input('Digite um novo numero inteiro: '))
            v2 =int(input('Digite outro novo numero inteiro: '))
        
        caso =int(input('SELECIONE UMA DAS OPÇÕES: '))
        
print("================================")
print("FIM DO PROGAMA")      
print("================================")      