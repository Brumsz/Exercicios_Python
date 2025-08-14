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
print(f'{"PRODUTOS":^40}')
print('-'*40 )

for c in range(0, len(produtos)):
    
    if c % 2 == 0:
        print(f'{produtos[c] :.<30}',end ='')
    else:
        print(f'R${produtos[c]:>7.2f}')
print('-'*40 )