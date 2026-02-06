velocidade = float(input('Qual a velocidade do carro? Km/h'))
multa = (velocidade - 80) * 7

if velocidade >= 80:
    print('Você foi multado em R${}'.format(multa))
else:
    print('Você passou a {}Km/h e não foi  multado.'.format(velocidade))