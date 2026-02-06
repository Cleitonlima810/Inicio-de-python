dias = float(input('Quantos dias você ficou com carro: '))
percorido = float(input('Quantos Km o carro percoreu: '))
pg = (dias * 60) + (percorido * 0.15)

print('O total a pagar é de R${:.2f}'.format(pg))