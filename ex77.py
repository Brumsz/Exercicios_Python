palavras = ('girassol', 'montanha', 'computador', 'janela', 'oceano', 'livro', 'bicicleta')

vg = 'AEIOUaeiou'
vogais = ''

for c in range(0,len(palavras)):
    if palavras[c] in vg:
        vogais += c
    
    print(vogais)
    vogais = ''    