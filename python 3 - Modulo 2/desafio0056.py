somaidade = 0
media = 0
maisvelho = 0
nomevelho = ''
totmulher = 0
for c in range(1, 5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade

    if c == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        totmulher = totmulher + 1

media = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))