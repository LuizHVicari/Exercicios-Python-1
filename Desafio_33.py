#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))
if(num1 == num2) or (num1 == num2) or (num2 == num3):
    print('Por favor, informe números diferentes')
if (num1 > num2) and (num1 > num3):
    print('Maior número: {}'.format(num1))
elif (num2 > num1) and (num2 > num3):
    print('Maior número: {}'.format(num2))
elif (num3 > num1) and (num3 > num2):
    print('Maior número: {}'.format(num3))
if (num1 < num2) and (num1 < num3):
    print('Menor número: {}'.format(num1))
elif (num2 < num1) and (num2 < num3):
    print('Menor número: {}'.format(num2))
elif (num3 < num1) and (num3 < num2):
    print('Menor número: {}'.format(num3))