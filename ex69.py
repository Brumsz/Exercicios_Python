print("-="*10)
print("CADASTRO DE PESSOAS")
print("-="*10)

maior = homens = mulhermenos20 = 0

while True:
    idade = int(input("Digite idade: "))

    Sexo = input('Digite o sexo[M/F]: ').upper().strip()[0] 
    if Sexo not in 'MmFf':
        Sexo = input('Digite o sexo[M/F]: ').upper().strip()[0]  
    
    if Sexo in 'Mm':
        homens += 1
    
    if idade >= 18:
        maior += 1
        
    if Sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
        
    opcao = input("Continuar cadastro?[S/N] ").upper().strip()[0] 
    
    if opcao not in 'SsNn': 
        opcao = input("Continuar cadastro?[S/N] ").upper().strip()[0]     
    
    if opcao in 'Nn':
        break         
    print('-='*10)
print(f"Foram cadastrados {homens} Homens, {maior} maiores de idade e {mulhermenos20} Mulhere(s) com menos de 20 anos.")    