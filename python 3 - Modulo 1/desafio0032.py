import calendar
from datetime import date

ano = int(input('Digite o ano que gostaria de saber se é bissexto: '))
verificacao = calendar.isleap(ano)

if verificacao == True:
    print('O ano de {} é bisexto. '.format(ano))
else:
    print('O ano de {} não é bisexto. '.format(ano))
