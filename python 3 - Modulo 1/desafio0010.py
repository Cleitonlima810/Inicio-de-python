print('Você pode comprar dolar, valor atual US$1,00 = R$3,27')

reais = float(input('Quantos reais você tem: R$'))

c = reais / 3.27

print('Seus R${:.2f}, pode comprar US${:.2f} dolar'.format(reais, c))