#nome = str(input('Qual seu nome: ')).strip().upper()

#if nome == 'CLEITON':
#    print('Que nome lindo você tem! ')
#else:
#    print('Seu nome é tão normal! ')
#print('Bom dia, {}'.format(nome))

#-----------------------------------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {}'.format(m))

if m >= 6.0:
    print('Parabéns você foi aprovado!')
else:
    print('Com media {}, você ficou de recuperação.'.format(m))
print('')