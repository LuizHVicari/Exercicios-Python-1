#Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros
m = float(input('Informe o valor em metros: '))
cm = m * 10 ** 2
mm = m * 10 ** 3
print('Cm: {},\nMm: {}'.format(cm, mm))