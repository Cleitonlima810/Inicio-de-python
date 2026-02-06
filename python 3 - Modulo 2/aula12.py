nome = str(input('Qual é seu nome: ')).strip().upper()
if nome == 'GUSTAVO':
    print('Que nome bonito')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem comum no Brasil. ')
elif nome in 'ANA CLAUDIA JESSICA':
    print('Belo nome feminino')
else:
    print('seu nome é normal')
print('Tenha um bom dia {}'.format(nome))
