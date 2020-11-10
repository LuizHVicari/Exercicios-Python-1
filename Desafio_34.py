#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$1.2500,00, calcule um aumento de 10%.
#Para salários inferiories ou iguais, o aumento é de 15%.
salario = float(input('Informe o salário: '))
if salario > 12500:
    salario = salario * 1.10
else:
    salario = salario * 1.15
print('Novo salario: {}'.format(salario))