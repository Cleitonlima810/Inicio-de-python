valor = float(input('Digite seu salario: R$'))
aumento = valor + (valor * 15 / 100)
print('Seu salario de {:.2f} com a nova promoção de 15% de aumento, vai ficar R${:.2f}'.format(valor, aumento))