valor = float(input('Digite o valor do produto: R$'))
desconto = valor - (valor * 5 / 100)
print('Com desconto de 5% porcento o preço do produto fica R${:.2f}'.format(desconto))
