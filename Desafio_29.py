#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite
vel = float(input('Qual a velocidade do carro? '))
if vel > 80.0:
    multa = int(round((vel - 80) * 7))
    print('Você foi multado no valor de {}R$, por estar {}Km/h mais rápido que o permitido'.format(multa, vel - 80))
else:
    print('Velocidade regular, você não foi multado')