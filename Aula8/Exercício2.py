nota = None 
notas = list()
while nota != -1:
    nota = float(input('Inserir nota: '))
    if nota != -1:
        notas.append(nota)

quantNotas = len(notas)
print ('Essa é a quantidade de notas inseridas: ', quantNotas)
print ('Essas são as notas ao lado da outra: \n', notas)

notasInversas = notas[::-1]
print ('Essas são as notas na ordem inversa uma abaixo da outra: ') 
for nota in notasInversas:
    print (nota)

somaNotas = sum(notas)
print ('Essa é a soma das notas: ', somaNotas)

mediaNotas = sum(notas)/quantNotas
print ('Essa é média das notas: ', mediaNotas)

notasAcimaMedia = 0
for nota in notas:
    if nota >= mediaNotas:
        notasAcimaMedia += 1
print ('Quantidade de notas acima da média: ', notasAcimaMedia)

notasAbaixoSete = 0
for nota in notas:
    if nota < 7:
        notasAbaixoSete += 1
print ('Quantidade de notas abaixo de 7: ', notasAbaixoSete)

print ('Esse é seu programa para as suas fucking notas, de nada')