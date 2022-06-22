# Faça  um  programa  que  receba  a  temperatura  média  
# de  cada  mês  do  ano  e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturase  mostre 
# todas  as  temperaturas  acima  da  média  anual, 
# e  em  que  mês  elas ocorreram (mostrar o mês por extenso: 
# 1 – Janeiro, 2 – Fevereiro, . . . )

mesesAno = ['Janeiro','Fevereiro','Março','Abril','Maio',
           'Junho','Julho','Agosto','Setembro','Outubro', 
           'Novembro','Dezembro']

temperaturaMes = []
temperaturasMeses = []
for mes in mesesAno:
    temperaturaMes.append(float(input(f'Insira a temperatura média do mês {mes}: ')))
print('Essas são as temperaturas médias de cada mês do ano:', temperaturaMes)

mediaTemperaturas = sum(temperaturaMes)/len(mesesAno)
print ('Essa é a temperatura média anual: ', mediaTemperaturas)

temperaturasAcimaMedia = {}
for i in range(len(temperaturaMes)):
    if temperaturaMes[i] > mediaTemperaturas:
        temperaturasAcimaMedia[mesesAno[i]] = temperaturaMes[i]
print (f'Meses de temperatura acima da média {temperaturasAcimaMedia}')