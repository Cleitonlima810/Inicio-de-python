import random

aluno1 = str(input('Primeiro aluno, digite seu nome: '))
aluno2 = str(input('Segundo aluno, digite seu nome: '))
aluno3 = str(input('Terceiro aluno, digite seu nome: '))
aluno4 = str(input('Quarto aluno, digite seu nome: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)

print('O aluno sorteado foi {}'.format(sorteio))