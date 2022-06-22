#Escreva um programa que receba um número e exiba a sequência de fibonacci;

import time
def fibonacci(numero):
    if numero <= 1:
        print('Cheguei na condição de parada')
        return numero
    print('Eu sou o número', numero)
    time.sleep(1)
    return (fibonacci(numero-1))+(fibonacci(numero-2))
print(fibonacci(5))