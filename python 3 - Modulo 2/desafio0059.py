from time import sleep

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opção = 0

while opção != 5:
    print('-=-' * 5)
    print('[1]Somar\n'
          '[2]Multiplicar\n'
          '[3]Maior\n'
          '[4]Novos Números\n'
          '[5]Sair do Programa')
    print('-=-' * 5)

    opção = int(input('Qual função deseja executar? '))

    if opção == 1:
        somar = num1 + num2
        print('-=-' * 25)
        print('A soma de {} + {} é {}.'.format(num1,num2,somar))
        print('-=-' * 25)
    elif opção == 2:
        multiplicar = num1 * num2
        print('-=-' * 25)
        print('O resultado de {} x {} é {}.'.format(num1,num2,multiplicar))
        print('-=-' * 25)
    elif opção == 3:
        if num1 > num2:
            print('-=-' * 25)
            print('O primeiro número {} é maior que o segundo {}.'.format(num1,num2))
            print('-=-' * 25)
        else:
            print('-=-' * 25)
            print('O segundo número {} é maior que o primeiro {}. '.format(num2, num1))
            print('-=-' * 25)
    elif opção == 4:
        print('PROGRAMA REINICIANDO...')
        sleep(3)
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(3)
        print('Finalizado com sucesso!')
    else:
        print('Opção inválida, tente novamente.')
        sleep(3)