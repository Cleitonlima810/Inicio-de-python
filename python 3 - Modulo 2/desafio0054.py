from datetime import date

anoatual = date.today().year
contmaior = 0
contmenor = 0

for c in range (1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = anoatual - nasc
    if idade >= 18:
        contmaior = contmaior + 1
    elif idade < 18:
        contmenor = contmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contmaior))
print('E também tivemos {} pessoas menores de idade'.format(contmenor))