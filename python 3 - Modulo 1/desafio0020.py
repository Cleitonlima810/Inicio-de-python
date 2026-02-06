import random

qta = int(input('Quantos alunos tem na sala? digite para resgitrar o nome deles? '))
alunos1 = []

for c in range(0, qta):
    nome = str(input('Digite o nome do aluno {}: '.format(c+1)))
    alunos1.append(nome)

random.shuffle(alunos1)

print('A sequencia de aprensetação ficou {}'.format(alunos1))