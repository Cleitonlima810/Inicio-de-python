n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
media = (n1 + n2) / 2

if media <= 5:
    print('Você foi reprovado visto que sua média foi {:.2f}.'.format(media))
elif media > 5 and media < 6.9:
    print('Você está de recuperação sua media de {} foi maior que 5 e menor que 6,9. '.format(media))
else:
    print('Você foi aprovado média {}, maior que 7, parabéns.'.format(media))