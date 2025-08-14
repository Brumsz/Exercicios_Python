print('Medias finais!')

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0 :
    print('Sua média foi de {}, você foi reprovado! '.format(media))

elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de {}, você esta de recuperação!'.format(media))    

else:
    print('Sua média foi de {}, parabens você esta aprovado!'.format(media))    