valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual valor do seu salário? R$'))
qanos = int(input('Quantos anos de financiamento? '))
parcelas = valorcasa / (qanos * 12)
trintasalario = (salario * 30 / 100)

if parcelas > trintasalario:
    print('O emprestimo foi negado, visto que ás parcelas de R${:.2f} passa de 30% do seu salario de R${:.2f} '.format(parcelas, salario))
elif parcelas <= trintasalario:
    print('Seu emprestimo foi aprovado com ás parcelas no valor de R${:.2f}'.format(parcelas))
print('Obrigado volte sempre.')
