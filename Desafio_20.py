#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('Ordem: ', alunos)