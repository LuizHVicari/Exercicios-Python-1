#Faça um programa que eia um ano qualquer e leia se ele é bissexto
ano = int(input('Qual o ano? '))
if ano % 4 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')