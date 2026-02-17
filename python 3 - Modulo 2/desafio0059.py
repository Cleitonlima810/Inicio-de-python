from time import sleep

num1 = 0
num2 = 0
num3 = -1

while num3 != 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    print('-=-' * 5)
    print('[1]Somar\n'
          '[2]Multiplicar\n'
          '[3]Maior\n'
          '[4]Novos Números\n'
          '[5]Sair do Programa')
    print('-=-' * 5)

    num3 = int(input('Qual função deseja executar? '))

    if num3 == 1:
        somar = num1 + num2
        print('-=-' * 25)
        print('Valor da somar entre {} e {} é igual a {}.'.format(num1,num2,somar))
        print('-=-' * 25)
    elif num3 == 2:
        multiplicar = num1 * num2
        print('-=-' * 25)
        print('Valor da multiplicação entre {} e {} é igual a {}.'.format(num1,num2,multiplicar))
        print('-=-' * 25)
    elif num3 == 3:
        if num1 > num2:
            print('-=-' * 25)
            print('O primeiro número {} é maior que o segundo {}.'.format(num1,num2))
            print('-=-' * 25)
        else:
            print('-=-' * 25)
            print('O segundo número {} é maior que o primeiro {}. '.format(num2, num1))
            print('-=-' * 25)
    elif num3 == 4:
        print('PROGRAMA REINICIANDO...')
        sleep(3)
    elif num3 == '':
        print('Ou você digitou letras ou não digitou nada, tente novamente.')
        sleep(3)
if num3 == 5:
    print('FIM DO PROGRAMA')