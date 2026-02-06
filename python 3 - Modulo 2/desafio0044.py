print('========LOJAS CLEITON==========')
preco = int(input('Preço das compras: R$'))
print('1 - À vista dinheiro ou cheque: 10% de desconto.\n'
      '2 - À vista cartão 5% de desconto.\n'
      '3 - Em até 2x no cartão, preço normal.\n'
      '4 - 3x ou mais no cartão 20%, de juros.')

opção = int(input('Qual a forma de pagamento? '))

if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparcela, parcela))
else:
    total = preco
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(preco, total))
