print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Segundo segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ESÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo!')





#Código acima do professor, eu não sabia do if dentro de if. kkkkkkkkk

#print('-='*20)
#print('Analisador de Triângulos')
#print('-='*20)

#r1 = float(input('Primeiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Segundo segmento: '))

#if r1 == r2 and r2 == r3 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Pode formar um tringulo equilatero.')
#elif (r1 == r2 or r2 == r3 or r3 == r1) and (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
#    print('Pode formar um tringulo isósceles.')
#elif r1 != r2 and r2 != r3 and r3 != r1 and r3 != r2 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Pode formar um tringulo escaleno.')