peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('Você está abaixo do peso IMC de {:.2f}.'.format(IMC))
elif IMC >= 18.5 and IMC < 25.0:
    print('Você está no peso ideal IMC de {:.2f}.'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('Você está com sobrepeso IMC de {:.2f}.'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('Você está com obesidade IMC de {:.2f}.'.format(IMC))
elif IMC >= 40:
    print('Você está em obesidade mórbida IMC de {:.2f}.'.format(IMC))
