vel = float(input('Digite a velocidade que você estava, se mentir: '))

if vel <= 80 :
    print('Parabens voce esta dentro do limite de velocidade de 80 km/h')
else:
    print('Uau,temos um corredor! Sua velocidade é de {}, você recebera uma multa que ira custar 7,00R$ por cada Km acima do limite'.format(vel))
    multa = (vel - 80) * 7
    print('Sua multa sera de {}R$'.format(multa))    