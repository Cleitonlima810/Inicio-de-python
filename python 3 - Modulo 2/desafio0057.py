sexo = str('').upper()

while sexo not in ('F', 'M'):
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
    if sexo not in ('F', 'M'):
        print('Sexo invalido. Tente novamente.')
if sexo == 'M':
    print('Sexo ({}) Masculino registrado com sucesso.'.format(sexo))
elif sexo == 'F':
    print('Sexo ({}) Feminino registrado com sucesso.'.format(sexo))
print('Fim')