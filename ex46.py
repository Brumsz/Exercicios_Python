from random import randint

numero  = randint(0,5)

res = int 

tent = 0

while res != numero:
    res = int(input('Digite um numero de 0 a 5 para ver se acerta: '))
    if res != numero:
        print('KKK você errou! Tente novaente')
    tent += 1

print('parabens você acertou! E precisou de {} tentativas. '.format(tent))

        