#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
n = float(input('Número: '))
n2 = n * 2
n3 = n * 3
n_raiz = n**(1/2)
print('Dobro: {},\nTriplo: {},\nRaiz quadrada: {}'.format(n2, n3, n_raiz))