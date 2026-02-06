num1 = int(input('Digite um número inteiro: '))

print('=' * 30)
convert = int(input('1 - Para Binario\n'
                    '2 - Para Octal\n'
                    '3 - Para Hexadecimal\n'
                    'Qual será a base qeu deseja usar: '))

if convert == 1:
    print('O número {} em binário fica {}.'.format(num1, bin(num1)[2:]))
elif convert == 2:
    print('O número {} em octal fica {}.'.format(num1, oct(num1)[2:]))
elif convert == 3:
    print('O número {} em hexadecimal fica {}.'.format(num1, hex(num1)[2:]))
else:
    print('Você digitou um número sem função, até a próxima.')