from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel]
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
'''
Acima o código do professor de forma melhorada.

import random

print('Vamos jogar Jokenpô.')
print('1 - Pedra\n')
print('2 - Papel\n')
print('3 - Tesoura')

num1 = int(input('Escolha sua opção: '))

aleatorio = random.randint(1, 3)

if aleatorio == num1:
    print('Deu empate eu escolhi o mesmo que você.')
elif aleatorio == 2 and num1 == 3:
    print('Você ganhou, escolheu Tesoura e eu escolhi papel.')
elif aleatorio == 1 and num1 == 2:
    print('Você ganhou, escolheu Papel e eu escolhi Pedra.')
elif aleatorio == 3 and num1 == 1:
    print('Você ganhou, escolheu Pedra e eu escolhi Tesoura.')
elif aleatorio == 3 and num1 == 2:
    print('Você perdeu, eu escolhi Tesoura e você escolheu Papel.')
elif aleatorio == 2 and num1 == 1:
    print('Você perdeu, eu escolhi Papel e você escolheu Pedra.')
elif aleatorio == 1 and num1 == 3:
    print('Você perdeu, eu escolhi Pedra e você escolheu Tesoura.')
else:
    print('Digite um valor entre 1 e 3, para iniciar o jogo.')'''