import random
from time import sleep

print('-=-' * 20)
print('vou pensar um número entre 0 e 5, tente adivinha qual número eu pensei.')
print('-=-' * 20)

num1 = random.randint(0,5)
num2 = float(input('Digite o número que você pensou: '))

print('PROCESSANDO...')
sleep(3)

if num1 == num2:
    print('Está correto você acertou')
else:
    print('Você errou eu escolhi o número {}'.format(num1))
