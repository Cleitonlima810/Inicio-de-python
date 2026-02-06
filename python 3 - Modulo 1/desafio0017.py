import math

num1 = float(input('Qual valor do cateto oposto: '))
num2 = float(input('Qual valor do cateto adjacente: '))

hipotenusa = math.hypot(num1, num2)

print('cateto oposto de {} + cateto adjacente de {} = hipotenusa de {:.2f} '.format(num1, num2, hipotenusa))