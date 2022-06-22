perguntasCrime = ['Telefonou para a vítima? ', 
                 'Esteve no local do crime? ', 
                 'Mora perto da vítima? ', 
                 'Devia para a vítima? ',            
                 'Já trabalhou com a vítima? ']

   
a = input(perguntasCrime[0])
b = input(perguntasCrime[1])
c = input(perguntasCrime[2])
d = input(perguntasCrime[3])
e = input(perguntasCrime[4])

classificaçãoCrime = ''
respostasCrime = [a,b,c,d,e]
respostasSim = respostasCrime.count('sim')

if respostasSim == 2:
    classificaçãoCrime = 'Você é suspeita'
elif respostasSim == 3:
    classificaçãoCrime = 'Você é cúmplice'
elif respostasSim == 4:
    classificaçãoCrime = 'Você é cúmplice'
elif respostasSim == 5:
    classificaçãoCrime = 'Você é um assasino'
else:
    classificaçãoCrime = 'Parabéns! Você é inocente'

print(classificaçãoCrime)





