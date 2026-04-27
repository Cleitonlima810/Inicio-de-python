sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()

while sexo not in ('F', 'M'):
    sexo = str(input('Sexo invalido. Digite seu sexo: [M/F] ')).strip().upper()
if sexo == 'M':
    print('Sexo ({}) Masculino registrado com sucesso.'.format(sexo))
elif sexo == 'F':
    print('Sexo ({}) Feminino registrado com sucesso.'.format(sexo))
print('Fim')