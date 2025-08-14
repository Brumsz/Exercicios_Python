print("Alistamento militar")

idade = int(input('Digite sua idade: '))


if idade == 18:
    print('Você tem 18 anos, ja esta na hora de se alistar!')

elif idade < 18:
    print('Você ainda não esta na idade de se alistar ainda faltam {} anos!'.format(18-idade))

else:
    print('Você ja passou da idade faz {} anos, procure a junta militar o mais rapido possivel!!'.format(idade-18))
            
