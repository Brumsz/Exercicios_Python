preço = float(input('Digite o preço do produto: '))
cond = int(input('Escolha a forma de pagamento sendo: \n 1- A vista no dinheiro \n 2- A vista no cartão \n 3- Em até 2 vezes no cartão \n 4- Em 3 ou mais vezes no cartão: '))

if cond == 1:
    preço =  preço - (preço * 0.10) 
    print('Você escolheu a vista no dinheiro, você teve um desconto de 10 %, e seu produto ficou {} R$' .format(preço))

elif cond == 2:
    preço =  preço - (preço * 0.05)
    print('Você escolheu a vista no cartão, você teve um desconto de 5 %, e seu produto ficou {} R$' .format(preço))    

elif cond == 3:
    preço = preço / 2
    print('Você escolheu em duas vezes no cartão, você teve desconto, e seu produto ficou em duas parcelas de {} R$' .format(preço))    

elif cond == 4:
    preço =  preço + (preço * 0.20)
    print('Você escolheu em 3 ou mais vezes no cartão, o produto teve mais 20% de juros, e seu produto ficou {} R$' .format(preço)) 

else:
    print('Insira uma das opções validas!')       
