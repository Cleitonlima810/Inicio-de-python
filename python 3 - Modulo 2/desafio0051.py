inicio = int(input('Primeiro termo: '))
paso = int(input('Razão: '))
decimo = inicio + (10 - 1) * paso
for i in range(inicio, decimo + paso, paso):
    print(i)
print('FIM')
