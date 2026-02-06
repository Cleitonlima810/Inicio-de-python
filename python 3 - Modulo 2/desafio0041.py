import datetime

nascimento = int(input('Qual seu ano de nascimento? '))
anoatual = datetime.date.today().year
idade = anoatual - nascimento

if idade <= 9:
    print('Você faz parte do time MIRIM, por tem {} anos.'.format(idade))
elif idade <= 14:
    print('Você faz parte do time INFANTIL, por tem {} anos.'.format(idade))
elif idade <= 19:
    print('Você faz parte do time JUNIOR, por tem {} anos.'.format(idade))
elif idade <= 20:
    print('Você faz parte do time SÊNIOR, por tem {} anos.'.format(idade))
elif idade > 20:
    print('Você faz parte do time MASTER, por tem {} anos.'.format(idade))
