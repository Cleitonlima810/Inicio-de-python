n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        elif n % 2 == 1:
            impar = impar + 1

print('Você digitou {} par e {} impar.'.format(par, impar))