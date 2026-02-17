import random
from time import sleep

print('-=-' * 20)
print('vou pensar um número entre 0 e 10, tente adivinha qual número eu pensei.')
print('-=-' * 20)

num2 = -1
num1 = -2

while num1 != num2:
    num1 = random.randint(0, 10)
    num2 = float(input('Digite o número que você pensou: '))

    if num1 != num2:
        print('PROCESSANDO...')
        sleep(1)
        print('Eu pensei no {}, e você digitou {}, vamos novamente.'.format(num1,num2))
if num1 == num2:
    print('PROCESSANDO...')
    sleep(1)
    print('-=-' * 20)
    print('Parabéns você ganhou, eu pensei no {}, e você digitou {}.'.format(num1,num2))
    print('FIM')
    print('-=-' * 20)
