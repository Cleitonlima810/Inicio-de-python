import math

num1 = float(input('Digite o angulo para caucular sen, cos, tg: '))

num1 = math.radians(num1)

print(' {:.2f}º Gruas \n sen {:.2f} \n cos {:.2f} \n tg {:.2f} '.format(num1, math.sin(num1), math.cos(num1), math.tan(num1)))
