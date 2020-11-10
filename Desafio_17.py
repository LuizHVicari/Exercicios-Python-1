#Faça um programa que leia o compriemnto do cateo oposto e do cateto adjacent de um triangulo retângulo, calcule e
#mostre o comprimento da hipotenusa
from math import pow, sqrt
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = sqrt(pow(ca, 2) + pow(co,2))
print('Hipotenusa: ', h)