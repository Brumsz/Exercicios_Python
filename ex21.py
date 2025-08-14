from random import randint

numero  = randint(0,5)

res = int(input('Digite um numero de 0 a 5 para ver se acerta: '))

if res == numero:
    print('parabens você acertou!')
else:
    print('KKK você errou')    