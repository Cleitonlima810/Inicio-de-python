soma = 0
cont = 0
for c in range(1, 500+1):
    if c % 3 == 0 and c % 2 == 1:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
