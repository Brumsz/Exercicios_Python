from random import randint
print("-="*10)
print("Vamos jogar par ou impar??".upper())

vitorias = 0 


while True:
    print("-="*10)
    jogador = int(input("Digite um numero: "))
    escolha = input("Escolha P ou I: ").strip().upper()[0]
    
    print("-="*10)
    
    if escolha not in "PpIi":
        print("Escolha invalida!")
        escolha = input("Escolha P ou I: ").strip().upper()[0]
        
        print("-="*10)
        
    
    comp = randint(0,10) 
    soma = jogador + comp
    res = soma % 2
    
    if res == 0:
        if escolha in 'Pp':
            print(f'Você escolheu {jogador} e o computador {comp}, a soma deu {soma}. Deu PAR!')
            print("Você ganhou!")
            
            vitorias += 1
        else:
            print(f'Você escolheu {jogador} e o computador {comp}, a soma deu {soma}. Deu PAR!')
            print(f"Você Perdeu! E você teve {vitorias} consecultivas.")
            break
    else:
        if escolha in 'Ii':    
            print(f'Você escolheu {jogador} e o computador {comp}, a soma deu {soma}. Deu IMPAR!')
            print("Você ganhou!")
            
            vitorias += 1
        else:
            print(f'Você escolheu {jogador} e o computador {comp}, a soma deu {soma}. Deu IMPAR!')
            print(f"Você Perdeu! E você teve {vitorias} consecultivas.")
            break    
    print("-="*10)    
    print('Jogar novamente...')    


        
    
    

        
        
       
