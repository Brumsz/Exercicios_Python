#enquanto o valor diitado for diferente de f ou m ,peça digitação novamente
sexo = str(input('Digite seu sexo[M/F]: '))

while sexo not in 'MmFf':
    sexo = str(input('Informação invalida! Digite seu sexo novamente[M/F]: ')).strip().upper()[0] 

print('O seu sexo é {}'.format(sexo))    