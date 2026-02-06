tabuada = int(input('Digite qual taboada: '))

for c in range(0, 10+1):
    print('{} x {} = {}'.format(c, tabuada, tabuada * c))
print('='*20)
for c in range(0, 10 + 1):
    print('{} + {} = {}'.format(c, tabuada, tabuada + c))
print('='*20)
for c in range(0, 10 + 1):
    print('{} - {} = {}'.format(c, tabuada, tabuada - c))
print('FIM')