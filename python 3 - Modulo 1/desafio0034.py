salario = float(input('Qual o seu salario: R$ '))

aumento1 = 10 * (salario / 100) + salario
aumento2 = 15 * (salario / 100) + salario

if salario >= 1250:
    print('Seu salario de {} recebeu um aumento de 10%, ficando no valor de R${}'.format(salario, aumento1))
else:
    print('Seu salario de {} recebeu um aumento de 15%, ficando no valor de R${}'.format(salario, aumento2))