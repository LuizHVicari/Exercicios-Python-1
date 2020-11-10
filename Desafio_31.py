#Desenvolva um programa que meça a dstância de uma viagem em Km. Calcule o prço da passagem cobrando R$0,50 por km em
#viagens até 200Km e R$0,45 para viagens mais longas
distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45
print('O valor da passagem será de R${}'.format(custo))