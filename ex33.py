print('Confederação nacional de Natação!')

idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Sua categoria é a Mirim!')

elif idade > 9 and idade <= 14:
    print('Sua categoria é a Infantil!')

elif idade > 14 and idade <= 19:
    print('Sua categoria é Junior!')

elif idade == 20:
    print('Sua categoria é Sênior!')

else:
    print('Sua categoria é Master!')                