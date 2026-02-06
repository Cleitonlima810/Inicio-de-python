import datetime

datahj = datetime.date.today().year
nascimento = int(input('Qual seu ano de nascimento: '))
idade = datahj - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, datahj))

if idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, falta {} anos para você fazer alistamento.'.format(saldo))
    ano = datahj + saldo
    print('Se alistamento vai ser em {}.'.format(ano))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!'.format(idade))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = datahj - saldo
    print('Seu alistmaneto foi em {}.'.format(ano))
else:
    print('Caso não tenha dado nem um resultado vc digitou letras, tente novamente.')