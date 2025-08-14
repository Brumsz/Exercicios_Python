l1 = float(input('Digite um valor de um lado do triangulo: '))
l2 = float(input('Digite um valor de outro lado do triangulo: '))
l3 = float(input('Digite um valor de mais outro lado do triangulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Pode se formar um triangulo.')
else:
    print('Não pode se formar um triangulo.')    