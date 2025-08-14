print('Progressão Aritimética')
print('-=' * 10)

primeiro = int(input("Digite o primeiro valor: "))
razao = int(input("Digite a sua razão: "))
termo = primeiro
cont = 1 
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print("{} ->" .format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos mais deseja ver? ")) 
print("FIM")       
    