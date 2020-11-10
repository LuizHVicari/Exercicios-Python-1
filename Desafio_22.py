#Crie um programa que leia o nome completo de uma pessoa e mmostre:
#->O nome com todas as letras maiúsiculas
#->O nome com todas minúsculas
#->Quantas letras no total (sem considerar espaços)
#->Quantas letras tem o primeiro nome
nome = input('Informe seu nome completo: ')
print('Seu nome com todas as letras maiusuclas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
aux = nome.replace(' ', '')
print('Quantidade de letras no seu nome: {}'.format(len(aux)))
aux2 = nome.split()
print('Quantidade de letras no seu primeiro nome: {}'.format(len(aux2[0])))
