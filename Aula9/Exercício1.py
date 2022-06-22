#Escreva um programa que receba um número e exiba o seu fatorial;
#Exemplo de recursividade

import time
def fatorial(numero):
    if numero == 0:
        print('Cheguei na condição de parada')
        return 1
    print('Eu sou o número', numero)
    time.sleep(1)
    return numero * fatorial(numero-1)
print(fatorial(5))
