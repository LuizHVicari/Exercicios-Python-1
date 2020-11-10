#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido
#Nesse exercício, assiti a resolução em vídeo par entender como resolver (até a parte de lista)
#link da resolução: https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=28
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 5: ')
alunos = [a1, a2, a3, a4]
print('O escolhido foi: {}'.format(alunos[random.randint(0, 3)]))