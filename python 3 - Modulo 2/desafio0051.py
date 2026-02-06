inicio = int(input('Digite o número de deseja iniciar a contagem: '))
fim = int(input('Digite o número final da contagem: '))
paso = int(input('Digite o número de quanto em quanto deseja contar: '))

for i in range(inicio, fim + 1, paso):
    if i <= 11:
        print(i)
print('FIM')