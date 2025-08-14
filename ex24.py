dis = float(input('Digite a distancia de sua viagem em KMs: '))

if dis <= 200:
    
    print('O preço da sua passagem sera de {} R$! ' .format(dis * 0.50))
else:
    
    print('O preço da sua passagem sera de {} R$! ' .format(dis * 0.45))