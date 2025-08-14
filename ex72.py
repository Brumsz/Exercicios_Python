
nuExtends = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

digi = int(input("Escreva um numero de 0 a 20: "))

while digi > 20 or digi < 0:
    digi = int(input("Digite um numero valido! Escreva um numero de 0 a 20: "))

print(f'Você digitou o numero {nuExtends[digi]}')