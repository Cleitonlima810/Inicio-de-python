print('=' * 40)
print('Digite dois número para comparar qual é maior entre eles.')
print('=' * 40)
num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))

if num1 > num2:
    print('O primeiro valor é maior número:{}'.format(num1))
elif num2 > num1:
    print('O segundo valor é maior número:{}'.format(num2))
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.'.format(num1, num2))
else:
    print('Você não digitou número.')
