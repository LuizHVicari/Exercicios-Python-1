#Escreva um progama que faça o computador "pensar" num número intiero de 0 a 5, e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
#Tive que colocar dessa maneira por com randint(0, 5) o programa só escolhia 5, não sei o porquê ainda
rand_ = randint(1, 6) - 1
num = int(input('Qual número o computador escolheu? '))
if(num  == rand_):
    print("Parabéns, você acertou!")
else:
    print('Você errou, o número escolhido foi {}'.format(rand_))