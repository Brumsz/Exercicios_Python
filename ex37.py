from random import choice
from time import sleep

print('JOKEMPO')

eu = str(input('Escolha entre pedra,papel ou tesoura: ')).upper()
lista = ['PEDRA','PAPEL','TESOURA']
comp = choice(lista)

sleep(2)

print('Preparado?')

sleep(2)

print('Vai!')

sleep(1)

print('O computador escolheu {}!'.format(comp))

sleep(1)

if eu == comp:
    print('Os dois escolheram {}, portanto...'.format(eu))
    sleep(1)
    print('Deu EMPATE!!')

elif eu == 'TESOURA' and comp == 'PAPEL' or eu == 'PAPEL' and comp == 'PEDRA' or eu == 'PEDRA' and comp == 'TESOURA':
    print('Você escolheu {} e o computador escolheu {}, portanto...'.format(eu,comp))
    sleep(1)
    print('Você GANHOU!!')
    
else:
    print('Você escolheu {} e o computador escolheu {}, portanto...'.format(eu,comp))
    sleep(1)
    print('Você PERDEU!!')
    
        



