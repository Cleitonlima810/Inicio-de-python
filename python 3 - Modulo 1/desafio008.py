metros = float(input('Digite quantos metros para converter: '))
cm = metros*100
mm = metros*1000
km = metros/1000

print('{} Metros. \nEm KM: {}KM \nEm centimetros é: {}cm \nEm milimetros é: {}mm '.format(metros, km, cm, mm))