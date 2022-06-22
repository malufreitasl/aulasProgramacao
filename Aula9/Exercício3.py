#Escreva um programa que calcule o exponencial de um número (receba o número e o exponencial como entrada);

numero = float(input('Inserir número: '))
expoente = float(input('Inserir expoente: '))

import time
def exponencial(numero,expoente):
    if numero <= 1:
        print('Cheguei na condição de parada')
        return 'Número inválido'
    if expoente == 0:
        print('Cheguei na condição de parada')
        return 1
    print('Eu sou o número', numero)
    time.sleep(1)
    return numero*(exponencial(numero,expoente-1))

print(exponencial(numero,expoente))