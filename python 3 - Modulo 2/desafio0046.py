from time import sleep

print('-=-'*20)
print('CONTAGEM REGRESSIVA')
print('-=-'*20)

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('-=-'*20)
print('\033[1;34;40mBUM! BUM! POOOW!\033[m')
print('-=-'*20)