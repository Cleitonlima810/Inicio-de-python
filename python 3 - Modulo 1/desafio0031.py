distancia = float(input('Quantos km tem sua viagem? '))
ate200k = distancia * 0.50
acima200k = distancia * 0.45

if distancia <= 200:
    print('sua viagem vai custar R${}'.format(ate200k))
else:
    print('Sua viagem vai custar R${}'.format(acima200k))
