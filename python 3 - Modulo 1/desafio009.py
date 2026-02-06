taboada =  float(input('Digite um número e veja sua taboada: '))

for i in range(0, 11):
        print(' {} x {:2} = {}'.format(taboada, i, taboada * i))