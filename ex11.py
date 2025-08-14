from math import sqrt,pow
op = int(input('Digite o valor do cateto oposto: '))
ad = int(input('Digite o valor do cateto adjascente: '))

hip= (pow(op,2)+pow(ad,2))
res = sqrt(hip)

print('A hipotenusa é {}'.format(res))
