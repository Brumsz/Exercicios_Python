print('Calculo de IMC!')
peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em Metros: '))

imc = peso/(altura * altura)

if imc < 18.5:
    print('Seu IMC é de {:.1f}, você esta abaixo do seu peso ideal!'.format(imc))

elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.1f}, você esta no seu peso ideal'.format(imc))

elif imc > 25 and imc <= 30:
    print('Seu IMC é de {:.1f}, você esta sobrepeso!'.format(imc))

elif imc > 30 and imc <=40:
    print('Seu IMC é de {:.1f}, você esta obeso!'.format(imc))

else:
    print('Seu IMC é de {:.1f}, você esta em obesidade morbida, procure ajuda!'.format(imc))    
                
    