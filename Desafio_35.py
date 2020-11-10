#Desenvolva um programa que leia o cumprimento de três de três retas e diga ao usuário se elas podem
#ou não formar um triângulo
r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('As retas {}, {} e {} podem formar um triângulo'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} não podem formar um triângulo'.format(r1, r2, r3))
