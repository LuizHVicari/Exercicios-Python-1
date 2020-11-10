#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra 'A', em que posição ela aparece
#pela primeira e última vez
frase = input('Insira a frase: ')
frase = frase.strip()
frase = frase.lower()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que "a" aparece é na posição {}'.format(frase.find('a') + 1))
print('A última vez que "a" aparece é na posição {}'.format(frase.rfind('a') + 1))