largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
quantidade = area / 2
print('Sua parede tem dimensão de {} x {} e sua área é de {}m². '.format(largura, altura, area))
print('Para pintar essa parede, você precisa de {}l de tinta. '.format(quantidade))