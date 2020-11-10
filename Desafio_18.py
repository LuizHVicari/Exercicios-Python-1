#Faça um programa que leia um ânglo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan
ang = float(input('Informe o ângulo: '))
ang_cos = cos(ang)
ang_sen = sin(ang)
ang_tg = tan(ang)
print('Seno: {}\nCosseno: {}\nTangente: {}'.format(ang_sen, ang_cos, ang_tg))