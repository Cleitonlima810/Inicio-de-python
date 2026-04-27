num1 = int(input('Digite um número: '))
cont = num1
resultado = 1
print('Calculando {}! = '.format(num1), end='')

while cont > 0:
    print('{} '.format(cont),end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')
    resultado = resultado * cont
    cont -= 1
print(resultado)



#Modelo do professor:

#from math import factorial
#n1 = int(input('Digite um número para calcular seu Fatorial:'))
#fact = factorial(n1)
#print('O fatorial de {} é: {}'.format(n1,fact))