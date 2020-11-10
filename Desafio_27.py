#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
#último nome separadamente.
completo = input('Informe seu nome completo: ')
completo = completo.strip()
primeiro = completo.split()
print('Seu primeiro nome é: {}'.format(primeiro[0]))
print('Seu último nome é: {}'.format(primeiro[completo.count(' ')]))