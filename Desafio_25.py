#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
nome = input('Informe seu nome:')
print(bool(nome.find('Silva')))