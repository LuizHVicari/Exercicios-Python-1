#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'
cidade = input('Informe o nome da cidade: ')
print('A cidade começa com Santo? {}'.format(cidade[:5] == 'Santo'))