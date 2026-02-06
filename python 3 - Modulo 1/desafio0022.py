nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é',nome.upper())
print('Seu nome em minusculas é',nome.lower())
print('Seu nome tem ao todo {} letas'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))]

separa = nome.split()

print('Seu Segundo nome é {} e ele tem {} letras'.format(separa[1], len(separa[1])))