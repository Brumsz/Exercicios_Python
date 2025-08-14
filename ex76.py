produtos = (
    'Coca-Cola', 4.50,
    'Lápis', 1.50,
    'Notebook', 2999.99,
    'Caneta', 2.00,
    'Caderno', 15.00,
    'Fone de Ouvido', 89.90,
    'Mochila', 120.00,
    'Celular', 1899.99,
    'Mouse', 49.99,
    'Teclado', 129.90
)

print('-'*40 )
print('PRODUTOS')
print('-'*40 )


for c in range(0, len(produtos),2):
    
    nome = produtos[c]
    preco = produtos[c+1]
    
    print(f'{nome}','.'*10 ,f'R${preco}')
   

print('-'*40 )
    
 
    
    