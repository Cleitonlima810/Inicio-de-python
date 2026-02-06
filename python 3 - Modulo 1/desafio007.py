nome = input('Qual o seu nome?')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
r = (n1+n2)/2
print('Olá {}, sua média dos dois bimestre é {:.1f}'.format(nome, r))