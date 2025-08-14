val = float(input('Digite o valor do seu salario para saber seu aumento: '))

if val > 1250 :
    print('O seu novo valor de salario é de {}R$ '.format(val + val * 0.10))
else:
    print('O seu novo valor de salario é de {}R$ '.format(val + val * 0.15))
               