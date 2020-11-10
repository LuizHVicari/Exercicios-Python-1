#Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
h = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura da parede: '))
a = h * l
q = a / 2
print('A parede tem área de {}m²'.format(a))
print('Para pintá-la, serão necessários {} L de tinta'.format(q))