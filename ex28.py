print('Aprovações de Emprestimos')
casa = float(input("Digite o valor da Casa que deseja comprar: "))
sal = float(input("Digite o valor do seu salario: "))
anos = int(input('Digite em quantos anos deseja pagar: '))

pres = sal - (sal * 0.3)
men = casa/sal
prest = casa/anos 

if anos < men:
    print('Você não conseguira pagar no tempo estimado. ')

elif prest > sal :
    print('Seu salario não cobre o emprestimo.')

else:
    print('Você pode fazer o emprestimo.')    
        


